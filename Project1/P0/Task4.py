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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
number_of_telemarketers=[]
for call in calls:
    if (call[0].startswith("140")) and (" " not in call[0][0:3]):
        if call[0] not in number_of_telemarketers:
            number_of_telemarketers.append(call[0])
print("These numbers could be telemarketers: ")
for number in number_of_telemarketers:
    print(number)


