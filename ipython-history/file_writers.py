import json
import os

def line_distances(data, username):
    file = open('output/'+username+'/line-distances.csv', 'w')
    file.write("\n".join(data))
    file.close()

def line_functions(data, username):
    file = open('output/'+username+'/line-functions.json', 'w')
    file.write(json.dumps(data, indent=2))
    file.close()

def line_function_count(data, username):
    file = open('output/'+username+'/line-function-count.csv', 'w')
    file.write("\n".join(data))
    file.close()

def submission_function_count(data, username):
    file = open('output/'+username+'/submission-functions.csv', 'w')
    file.write("\n".join(data))
    file.close()

def function_summary(data, username):
    data.sort()
    file = open('output/'+username+'/function-summary.json', 'w')
    file.write(json.dumps(data, indent=2))
    file.close()

def results(data, username):
    file = open('output/'+username+'/results.json', 'w')
    file.write(json.dumps(data, indent=2))
    file.close()

def group_count(data, username):
    output_csv = []
    output_csv.append("group_id,count")
    for key in data:
        value = str(data[key])
        output_csv.append(','.join([key, value]))

    file = open('output/'+username+'/group-count.json', 'w')
    file.write(json.dumps(data, indent=2))
    file.close()

    file = open('output/'+username+'/group-count.csv', 'w')
    file.write("\n".join(output_csv))
    file.close()

def group_lines(data, username):
    file = open('output/'+username+'/group-lines.json', 'w')
    file.write(json.dumps(data, indent=2))
    file.close()

def group_functions(data, username):
    output_json = dict()
    output_csv = []
    output_csv.append("group_id|functions")

    for key in data:
        values = data[key]
        values.sort()
        output_json[key] = ','.join(values)
        output_csv.append('|'.join([
            key,
            ','.join(values)
        ]))

    file = open('output/'+username+'/group-functions.json', 'w')
    file.write(json.dumps(output_json, indent=2))
    file.close()

    file = open('output/'+username+'/group-functions.csv', 'w')
    file.write("\n".join(output_csv))
    file.close()

def summary(data, username):
    output = dict()
    file = open('output/'+username+'/summary.json', 'w')
    file.write(json.dumps(data, sort_keys=False, indent=2))
    file.close()
