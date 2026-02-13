#!/usr/bin/python3
"""
Converting CSV Data to JSON Format module.
The objective is to gain experience in reading data from one format (CSV)
and converting it into another format (JSON) using serialization techniques.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV data to JSON format.

    This function reads a CSV file and converts it to JSON format,
    saving the result to 'data.json'.

    Args:
        csv_filename (str): The name of the CSV file to convert

    Returns:
        bool: True if the conversion was successful, False otherwise
    """
    try:
        # Open and read the CSV file
        with open(csv_filename, 'r') as csv_file:
            # Use DictReader to convert each row into a dictionary
            csv_reader = csv.DictReader(csv_file)
            # Convert to list of dictionaries
            data = list(csv_reader)

        # Write the serialized JSON data to data.json
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
