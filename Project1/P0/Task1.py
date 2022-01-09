"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
num_of_numbs=[]
for record in texts:
    num_of_numbs.extend(record[0:2])
for record_1 in calls:
    num_of_numbs.extend(record_1[0:2])
print("There are {} different telephone numbers in the records.".format(len(set(num_of_numbs))))   