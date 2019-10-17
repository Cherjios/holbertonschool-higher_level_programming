#!/usr/bin/python3
import sys
import os.path
import json

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

file = "add_items.json"
python_list = []

if os.path.exists(file):
    python_list = load_from_json_file(file)

for i in range(1, len(sys.argv)):
    python_list.append(sys.argv[i])

save_to_json_file(python_list, file)
