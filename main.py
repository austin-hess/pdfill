import sys
import os
import json
from pdfformfields import fill_form_fields, generate_dictionary

def parse_request(result_map, request, prev_key):
    print('Call parse_request')
    for key, val in request.items():
        print('{}: {}'.format(key, val))
        if type(val) is dict:
            next_key = '{}.{}'.format(prev_key, key) if prev_key != '' else key
            parse_request(result_map, val, next_key)
        else:
            map_key = key if prev_key == '' else '{}.{}'.format(prev_key, key)
            result_map[map_key] = val

def build_final_mapping(field_mapping, value_map):
    result_map = {}
    for key, val in field_mapping.get('fields').items():
        value = value_map.get(key)
        if value is not None:
            result_map[val] = value
    return result_map

input_filename = sys.argv[1]
input_doc_name = sys.argv[2]
mappings_file = sys.argv[3]
request_file = sys.argv[4]
output_filename = input_filename.replace('.pdf', '') + '_filled.pdf'

mapping = json.load(open(mappings_file, 'rb'))

doc_mapping = mapping.get(input_doc_name)

if doc_mapping is None:
    raise RuntimeError("Could not find a mapping for document named: '{}'".format(input_doc_name))

request = json.load(open(request_file, 'rb'))

value_map = {}
parse_request(value_map, request, '')
json.dump(value_map, open('./result.json', 'w'))
form_fields = build_final_mapping(doc_mapping, value_map)

print(form_fields)

fill_form_fields(input_filename, form_fields, output_filename)