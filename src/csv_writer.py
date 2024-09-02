# src/csv_writer.py

import csv

def write_to_csv(filename, data):
    """
    Writes the data to a CSV file.

    :param filename: Name of the CSV file to write to.
    :param data: A dictionary where keys are headers and values are lists of text content.
    """
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        
        # Write the headers
        headers = list(data.keys())
        csv_writer.writerow(headers)
        
        # Write the content rows
        rows = zip(*data.values())  # Combine values by row
        for row in rows:
            csv_writer.writerow(row)

