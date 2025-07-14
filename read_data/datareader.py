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

import csv

class Read:
    def get_csv_data(file_name):
        rows = []
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            for row in reader:
                if row and any(cell.strip() for cell in row):  # skip completely empty lines
                    rows.append(tuple(row))
        return rows
