import csv


with open("wijk_1.csv", "r") as csv_file:
    next(csv_file)
    reader = csv.reader(csv_file)

    for row in reader:
        data = row
    csv_file.close()

