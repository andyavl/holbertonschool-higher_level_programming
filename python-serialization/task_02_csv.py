#!/usr/bin/env python3
"""
This module provides functionality to convert data from a CSV file
to a JSON file.
"""

import csv
import json


def convert_csv_to_json(csv_file):
    """
    Converts the contents of a CSV file to a JSON file.

    Reads data from the specified CSV file and writes it as a list
    of dictionaries into a new file named 'data.json'.

    Args:
        csv_file (str): The path to the input CSV file.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_file, "r") as csv_f:
            read = csv.DictReader(csv_f)
            data = list(read)

        with open("data.json", "w") as json_f:
            json.dump(data, json_f)

        return True
    except (FileNotFoundError, Exception):
        return False
