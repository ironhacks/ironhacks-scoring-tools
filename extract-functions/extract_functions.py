#!/usr/bin/env python3

import os
import sys
import re
import argparse
import ast
import json
from collections import deque

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


def unique(list1):
    list_set = set(list1)
    unique_list = (list(list_set))
    return unique_list


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


def array_diff(prev_list, curr_list):
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



def write_function_summary(data, hack, submission, user):
    data.sort()
    summary_file = '/'.join([
        'data',
        hack,
        'submissions',
        submission,
        user,
        'submission_prediction_functions.json'
    ])
    summary_file2 = '/'.join([
        'data',
        hack,
        'submissions',
        submission,
        user,
        'submission_prediction_functions.js'
    ])

    results_path = '/'.join([
        'data',
        hack,
        'results',
        submission,
        'function-count',
    ])

    results_file = results_path + '/' + user + '.csv'

    if not os.path.exists(results_path):
        os.makedirs(results_path)

    file1a = open(summary_file, 'w')
    file1a.write(json.dumps(data))
    file1a.close()

    summary_text = "\"" + user_id + "\": " + json.dumps(data) + ",\n"

    file1b = open(summary_file2, 'w')
    file1b.write(summary_text)
    file1b.close()

    results_header = 'userId,functions'
    results_row = user + ',' + str(len(data))

    file2 = open(results_file, 'w')
    file2.write('\n'.join([results_header, results_row, '']))
    file2.close()




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user', help='user [USER_ID]', required=True)
    parser.add_argument('-H', '--hack', help='hack [HACK_ID]', required=True)
    parser.add_argument('-s', '--submission', help='submission [SUBBMISSION_ID]', required=True)

    args = parser.parse_args()

    submission_id = args.submission
    hack_id = args.hack
    user_id = args.user

    input_file = '/'.join([
        'data',
        hack_id,
        'submissions',
        submission_id,
        user_id,
        'submission_prediction_output.py'
    ])

    print('Extracting functions ', 'Hack: ', hack_id, ' Submission:', submission_id, ' User:', user_id)

    tree = ast.parse(open(input_file).read())
    nodes = get_tree_nodes(tree)
    nodes.sort()

    write_function_summary(nodes, hack_id, submission_id, user_id)
