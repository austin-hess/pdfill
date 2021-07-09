import sys
import os
import json
from pdfformfields import fill_form_fields, generate_dictionary

TEMP_DIR = 'temp'
CONFIG_DIR = 'config'
TEMP_FILE = './{}/temp.txt'.format(TEMP_DIR)
INPUT_PDF_PATH = './resources/fw8ben.pdf'
INPUT_PDF_LABEL = 'w8ben'
REFERENCE_PDF_PATH = './{}/config_pdf.pdf'.format(CONFIG_DIR)
FIELD_MAPPING_FILE = './{}/field_mapping.json'.format(TEMP_DIR)
USER_CONFIG_FILE = './{}/{}_config.json'.format(CONFIG_DIR, INPUT_PDF_LABEL)

fields = {}

if not os.path.isdir(TEMP_DIR):
    os.mkdir(TEMP_DIR)
if not os.path.isdir(CONFIG_DIR):
    os.mkdir(CONFIG_DIR)

with open(TEMP_FILE, 'w') as temp:
    original_stdout = sys.stdout
    sys.stdout = temp
    generate_dictionary(INPUT_PDF_PATH)
    sys.stdout = original_stdout

with open(TEMP_FILE, 'r') as temp:
    file_lines = temp.readlines()
    file_lines.pop(0)
    file_lines.pop(-1)
    for i, line in enumerate(file_lines):
        line = line.replace('"','').split(':')[0].strip()
        print(line)
        fields[str(i)] = line

with open(FIELD_MAPPING_FILE, 'w') as f:
    f.write(json.dumps(fields));

for key in fields.keys():
    fields[key] = 'TARGET PATH'

with open(USER_CONFIG_FILE, 'w') as f:
    f.write(json.dumps(fields))

fill_form_fields(INPUT_PDF_PATH, fields, REFERENCE_PDF_PATH)
