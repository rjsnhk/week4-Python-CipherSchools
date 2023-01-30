from csv import DictReader,DictWriter
with open('file.csv','r')as rf:
    with open('file.csv','w')as wf:
        csv_reader = DictReader(rf)
        csv_writer = DictWriter(wf,fieldnames=['first_names','last_names','age'])
        csv_writer.writeheader()
        for row in csv_reader:
            fname,lname,age=row['firstname'],row['lastname'],row['age']
            csv_writer.writerow({
                'firstname':fname.upper(),
                'lastname':lname.upper(),
                'age':age
            })
