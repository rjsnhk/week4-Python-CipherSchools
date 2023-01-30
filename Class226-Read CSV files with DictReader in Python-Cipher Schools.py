from csv import DictReader
with open('file.csv','r') as f:
    csv_reader = DictReader(f)
    for row in csv_reader:
        print(row['email'])