import csv

with open("input.txt", "r") as input_list:
    data = list(csv.reader(input_list))
    print(data)