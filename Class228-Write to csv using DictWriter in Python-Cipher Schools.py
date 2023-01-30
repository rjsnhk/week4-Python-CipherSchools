from csv import Dictwriter
with open('file1.csv','w',newline='') as f:
    csv_writer = Dictwriter(f,fieldnames=['firstnames','lastnames','age'])
    csv_writer.writeheader()
    csv_writer.writerow({
        'firstname':'harshit',
        'lastname':'vashistha',
        'age':20
    })
    csv_writer.writerow({
        'firstname':'mohit',
        'lastname':'vashistha',
        'age':20
    })