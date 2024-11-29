# demo_generator.py by james270tx
#
# This file creates a csv of 100 random customer id's selected from customers-1000.csv for demoing csv_lookup.py

import csv
import random

# for readability, customer_id is column B of the input csv; the index is 1
CUST_ID = 1

# reading all customer ids from infile
all_customer_id = []
count = 0
infile = "customers-1000.csv"
with open(infile,'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    for each_record in csv_reader:
        all_customer_id.append(each_record[CUST_ID])
        count += 1
print("Customer records read", count)

# append 100 customer ids to random_selection
random_selection = []
count = 0
for r in range(100):
    random_choice = random.randrange(1,1000)
    random_selection.append(all_customer_id[random_choice])
    count += 1
print(count,"random ids selected")

# write random_selection to outfile
count = 0
outfile = "demo_input.csv"
with open(outfile,'w',newline='') as write_obj:
    csv_writer = csv.writer(write_obj)
    for r in random_selection:
        this_row = [r]
        csv_writer.writerow(this_row)
        count += 1
write_obj.close()
print(count,"ids written to",outfile)