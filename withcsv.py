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

from datetime import datetime, timedelta
now =datetime.now() # this will give the current time 
yesterday= now -timedelta(days=1)
print(yesterday)

#i want the program to sleep for some time 
import time 
print(time.time())

#maing program to sleep for 2 sec 
time.sleep(2)
print(time.time())

          