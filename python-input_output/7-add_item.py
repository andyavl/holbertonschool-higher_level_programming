#!/usr/bin/python3
"""
Script that saves command-line arguments to a JSON file.

This script:
- Accepts command-line arguments (excluding the script name itself).
- Saves them into a JSON file named 'add_item.json'.
- Then loads the contents of the file back into a Python object.
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


arg_list = sys.argv[1:]

filename = "add_item.json"

save_to_json_file(arg_list, filename)

load_from_json_file(filename)
