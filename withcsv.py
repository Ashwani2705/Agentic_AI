import csv 

with open('data.csv',mode='w',newline='') as file:
    write =csv.writer(file)
    write.writerow(['name', 'age', 'city'])
    write.writerow(['John', 30, 'New York'])

#now we have to read the csv file which we will be doing using the csv module

with open('data.csv',mode='r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
          