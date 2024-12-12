def read_file_to_list(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

file_name = "example.txt"
lines_list = read_file_to_list(file_name)
print(lines_list)

def copy_odd_lines(source_file, destination_file):
    with open(source_file, 'r') as source, open(destination_file, 'w') as dest:
        for i, line in enumerate(source):
            if i % 2 != 0:
                dest.write(line)

source_filename = "source1.txt"
destination_filename = "odd_lines.txt"
copy_odd_lines(source_filename, destination_filename)

import csv
def read_csv_rows(filename):
    rows = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            rows.append(",".join(row))
    return rows

csv_filename = "example.csv"
rows_list = read_csv_rows(csv_filename)
print(rows_list)
