"""
Write a program csvstat that takes two commandline arguments: the name of a CSV
file and a column number. The specified column in the CSV file should contain
numbers. The program should print the total, min, max and avg of the numbers in
the specified column.
Example: csvstat input.csv 3
input.csv:
  Country,Capital,Districts
  Ireland,Dublin,4
  Germany,Berlin,9
  France,Paris,6
Output:
  total=19
  min=4
  max=6
  avg=6.3333
"""
import csv
import sys


# Read file function definition.
def read_file(csv_file, column):
    # Variables declaration
    values = []
    count_lines = 0
    # Open the csv file.
    with open(csv_file) as f:
        # Declare and initiate a csv reader.
        csv_reader = csv.reader(f, delimiter=',')
        # Iterate over each row of the file and add each value to the list.
        for row in csv_reader:
            # Schip the header line.
            if count_lines == 0:
                count_lines += 1
                pass
            else:
                # Increment the count lines variable and append the values to the list.
                count_lines += 1
                values.append(int(row[column]))
    # Calculate the output values.
    total_val = sum(values)
    min_val = min(values)
    max_val = max(values)
    avg = round(total_val / len(values), 4)
    print(f'total={total_val}\nmin={min_val}\nmax={max_val}\navg={avg}')


def main(data, column):
    read_file(data, column)


if __name__ == '__main__':
    data = sys.argv[1]
    column = int(sys.argv[2])
    main(data, column)
