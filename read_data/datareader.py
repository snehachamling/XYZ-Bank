# import csv
#
#
# class Read:
#     def get_csv_data(file_name):
#         rows = []
#         with open(file_name, 'r') as f:
#             reader = csv.reader(f)
#             next(reader)  # skip header
#             for row in reader:
#                 rows.append(tuple(row))
#         return rows

# import csv
#
# class Read:
#     def get_csv_data(file_name):
#         rows = []
#         with open(file_name, 'r') as f:
#             reader = csv.reader(f)
#             next(reader)  # skip header
#             for row in reader:
#                 if row and any(cell.strip() for cell in row):  # skip completely empty lines
#                     rows.append(tuple(row))
#         return rows

import csv
import os


class Read:
    @staticmethod
    def get_csv_data(file_name):
        # Get the directory two levels up (assumes this file is in something like read_data/)
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_path = os.path.join(project_root, 'testdata', file_name)

        print(f"Loading CSV data from: {csv_path}")  # Helpful debug log

        rows = []
        with open(csv_path, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            for row in reader:
                if row and any(cell.strip() for cell in row):  # skip empty lines
                    rows.append(tuple(row))
        return rows
