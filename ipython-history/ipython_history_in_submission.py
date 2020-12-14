#!/usr/bin/env python3

import os
import sys
import re
import argparse
import ast
import editdistance
import base64
import hashlib
import json
import IPython
from collections import deque
import file_writers as writer

SCRIPT_VERSION = "1.4.0"
HISTORY_MAX = 10000
MAX_LINE_LEN = 30000
HEAD_LENGTH = 20


def get_ipython_history(history_file):
    print("Reading history archive")
    hist = IPython.core.history
    ha = IPython.core.history.HistoryAccessor(hist_file=history_file)
    return ha.get_tail(HISTORY_MAX)


def unique(list1):
    list_set = set(list1)
    unique_list = (list(list_set))
    return unique_list


def create_output_dir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)


class FuncCallVisitor(ast.NodeVisitor):
    def __init__(self):
        self._name = deque()

    @property
    def name(self):
        return '.'.join(self._name)

    @name.deleter
    def name(self):
        self._name.clear()

    def visit_Name(self, node):
        self._name.appendleft(node.id)

    def visit_Attribute(self, node):
        try:
            self._name.appendleft(node.attr)
            self._name.appendleft(node.value.id)
        except AttributeError:
            self.generic_visit(node)


def get_tree_nodes(tree):
    nodes = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            call_visitor = FuncCallVisitor()
            call_visitor.visit(node.func)
            nodes.append(call_visitor.name)
        if isinstance(node, ast.Import):
            nodes.append('import')
    nodes.sort()
    return unique(nodes)


def get_submission_data(submission_file):
    with open(submission_file) as submission_file_data:
        submission_data = json.load(submission_file_data)
        return submission_data


def line_function_diff(prev_list, curr_list):
    added = []
    removed = []
    for item in curr_list:
        if item not in prev_list:
            added.append(item)
    for item in prev_list:
        if item not in curr_list:
            removed.append(item)

    return {
        'added': added,
        'removed': removed
    }

def functions_not_in_submission(all_functions, submission_functions):
    extra = []
    for item in all_functions:
        if item not in submission_functions:
            extra.append(item)
    return extra

def process_data(content, submission_data):
    submission_data_count = len(submission_data)
    counter = 0
    error_count = 0
    group_count = dict()
    group_code = dict()
    group_functions = dict()

    functions = []
    line_functions = []
    line_function_count = []
    line_function_count.append(",".join([
        'index',
        'command_id',
        'group_id',
        'added',
        'removed',
        'function_count',
        'cumulative',
    ]))
    line_distances = []
    line_distances.append(",".join([
        'index',
        'command_id',
        'group_id',
        'command_len',
        'editdistance',
    ]))
    results = []
    results.append([
        'command_id',
        'session',
        'index',
        'length',
        'distance',
        'group_id',
        'functions',
        'functions_added',
        'functions_removed',
    ])
    submission_completion = []
    submission_completion.append(",".join([
        'index',
        'group_id',
        'command_functions',
        'submission_functions',
        'cumulative',
        'percent_completion',
    ]))

    for line in content:
        if counter % 100 == 0:
            print('Processing line: ', counter)

        session = line[0]
        line_source = line[2]
        index = line[1]
        length = len(line_source)
        hash = hashlib.sha1(line_source[:MAX_LINE_LEN].encode('utf-8')).hexdigest()
        code = '\n'.join(line_source.split('\\n'))
        clean_line = re.sub("#.*", "", code)
        head = line_source.replace(" ", "").replace("\n", "")[0:HEAD_LENGTH]
        group_id = base64.b32encode(head.encode('utf-8')).decode()

        if (group_id in group_count):
            group_count[group_id] += 1
        else:
            group_count[group_id] = 1

        try:
            tree = ast.parse(clean_line)
            nodes = get_tree_nodes(tree)
            nodes.sort()
            functions += nodes
            functions = unique(functions)
        except:
            error_count += 1
            nodes = []

        if (group_id in group_code):
            prev_line = group_code[group_id][-1][1]
            prev_functions = group_code[group_id][-1][2]
            distance = editdistance.eval(prev_line[:MAX_LINE_LEN], line_source[:MAX_LINE_LEN])
        else:
            group_code[group_id] = []
            group_functions[group_id] = []
            prev_functions = []
            distance = 0

        unique_group_functions = unique(group_functions[group_id] + nodes)
        unique_group_functions.sort()
        group_functions[group_id] = unique_group_functions
        function_diff = line_function_diff(prev_functions, nodes)

        group_code[group_id].append([
            hash,
            line_source,
            nodes
        ])

        line_distances.append( ",".join([
            str(counter + 1),
            hash,
            group_id,
            str(length),
            str(distance),
        ]))

        line_functions.append([
            hash,
            nodes,
        ])

        line_function_count.append(",".join([
            str(counter + 1),
            hash,
            group_id,
            str(len(function_diff['added'])),
            str(len(function_diff['removed'])),
            str(len(nodes)),
            str(len(functions)),
        ]))

        functions_in_submission = []
        for func in functions:
            if func in submission_data:
                functions_in_submission.append(func)

        submission_completion.append(",".join([
            str(counter + 1),
            group_id,
            str(len(nodes)),
            str(len(functions_in_submission)),
            str(len(functions)),
            str(round(len(functions_in_submission) / submission_data_count, 2)),
        ]))

        result = []
        result.append(hash)
        result.append(session)
        result.append(counter + 1)
        result.append(length)
        result.append(distance)
        result.append(group_id)
        result.append(nodes)
        result.append(function_diff['added'])
        result.append(function_diff['removed'])
        results.append(result)
        counter += 1

    extra_functions = functions_not_in_submission(functions, submission_data)
    print("Done")

    summary = dict({
        "username": username,
        "total_commands": counter,
        "total_errors": error_count,
        "command_groups": len(group_code),
        "unique_functions": len(functions),
        "unused_functions": len(extra_functions),
    })

    print(json.dumps(summary, sort_keys=False, indent=2))

    print("extra_functions", extra_functions)

    writer.summary(summary, username)
    writer.line_distances(line_distances, username)
    writer.line_functions(line_functions, username)
    writer.line_function_count(line_function_count, username)
    writer.function_summary(functions, username)
    writer.results(results, username)
    writer.group_lines(group_code, username)
    writer.group_functions(group_functions, username)
    writer.group_count(group_count, username)
    writer.submission_function_count(submission_completion, username)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user', help='user [USER_ID]', required=True)
    parser.add_argument('-H', '--hack', help='hack [HACK_ID]', required=True)
    parser.add_argument('-s', '--submission', help='submission [SUBBMISSION_ID]', required=True)

    parser.add_argument('-i', '--input', help='Input [filename]', required=True)

    args = parser.parse_args()

    submission_id = args.submission
    hack_id = args.hack
    user_id = args.user

    history_file_in = args.input

    submission_file = args.submission

    username = history_file_in.split('/')[-1].replace('.sqlite', '')

    print("Processing user history file:", username)

    content = get_ipython_history(history_file_in)
    submission_data = get_submission_data(submission_file)
    submission_data.sort()
    submission_data = unique(submission_data)

    create_output_dir('output/'+username)
    process_data(content, submission_data)
