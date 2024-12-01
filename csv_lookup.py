# csv_lookup.py by james270tx
# 
# This is used to lookup records of one csv from another
# customers-1000.csv is the master list containing all details
# demo-input.csv is the list of ids we intend to look up
# summary.csv is the results showing details to match each id that we have looked up
# demo_generator.py creates a random csv of 100 customer ids to use as querys for the lookup

import csv

# for readability, the column/list indexes are used as constants
CUST_ID = 1
LAST_NAME = 3
COMPANY = 4
SUB_DATE = 10
CUST_QUERY = 0

# read lists of id, name, company, and subscription from reference file
customer_id = []
customer_name = []
company_name = []
subscription_date = []
count = 0
infile = "customers-1000.csv"
with open(infile,'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    for each_record in csv_reader:
        customer_id.append(each_record[CUST_ID])
        customer_name.append(each_record[LAST_NAME])
        company_name.append(each_record[COMPANY])
        subscription_date.append(each_record[SUB_DATE])
        count += 1
print(count,"reference records read from",infile)

# read list if customers to query and initialize the index list
customer_query = []
customer_index = []
count = 0
infile = "demo_input.csv"
with open(infile,'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    for each_record in csv_reader:
        customer_query.append(each_record[CUST_QUERY])
        customer_index.append("")
        count += 1
print(count,"demo records read from",infile)

# find the index of each customer id
count = 0
for i in range(0,len(customer_query)):
    if customer_query[i] in customer_id:
        customer_index[i] = customer_id.index(customer_query[i])
        count += 1
print(count,"customer ids found")

# send output to summary.csv
count = 0
outfile = "summary.csv"
with open(outfile,'w',newline='') as write_obj:
    csv_writer = csv.writer(write_obj)
    print("Writing headers to",outfile)
    this_row = ["Index","Customer Id","Last Name","Company","Subscription Date"]
    csv_writer.writerow(this_row)
    count += 1
    for i in range(0,len(customer_query)):
        r = customer_index[i] # r is used below instead of i as it is pertains to the index on the reference file
        this_row = [customer_index[i],customer_query[i],customer_name[r],company_name[r],subscription_date[r]]
        csv_writer.writerow(this_row)
        count += 1
write_obj.close()
print(count,"rows written to",outfile)