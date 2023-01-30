from csv import writer
with open('files.csv','w') as f:
    csv_writer = writer(f)
    csv_writer.writerow(['name','country'])
    csv_writer.writerow(['Aniket','INDIA'])
    csv_writer.writerow(['Harshit','INDIA'])