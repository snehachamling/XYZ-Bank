import csv


class Read:
    def get_csv_data(file_name):
        rows = []
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            for row in reader:
                rows.append(tuple(row))
        return rows