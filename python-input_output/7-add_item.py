#!/usr/bin/python3
"""
Script that saves command-line arguments to a JSON file.

This script:
- Accepts command-line arguments (excluding the script name itself).
- Loads existing data from 'add_item.json' if it exists.
- Appends new arguments to the list.
- Saves the updated list to 'add_item.json'.
"""

import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
arg_list = sys.argv[1:]

if os.path.exists(filename):
    try:
        data = load_from_json_file(filename)
    except Exception:
        data = []
else:
    data = []

data.extend(arg_list)

save_to_json_file(data, filename)
