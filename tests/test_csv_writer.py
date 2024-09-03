# tests/test_csv_writer.py

import os
import csv
import pytest
from src.csv_writer import write_to_csv

def test_write_to_csv(tmp_path):
    # Define a sample data dictionary
    data = {
        'header': ['h1 content', 'h2 content'],
        'paragraph': ['p1 content', 'p2 content']
    }
    
    # Define the output CSV file path
    output_file = tmp_path / "output.csv"
    
    # Call the function
    write_to_csv(output_file, data)
    
    # Read the content of the written CSV file
    with open(output_file, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        
        # Assert that the headers are correct
        headers = next(csv_reader)
        assert headers == ['header', 'paragraph']
        
        # Assert that the content rows are correct
        rows = list(csv_reader)
        assert rows == [
            ['h1 content', 'p1 content'],
            ['h2 content', 'p2 content'],
        ]

    # Clean up the generated file (optional since we are using tmp_path)
    os.remove(output_file)

