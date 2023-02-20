import csv
from pathlib import Path


def read_data():
    p = Path(__file__).with_name('./obesity_data_set.csv')
    with open(p, mode='r') as file:
        csvFile = csv.reader(file)
        num = 0
        for line in csvFile:
            if num < 1:
                print(line)
            num += 1
