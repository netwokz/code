# importing csv module
import csv

# csv file name
filename = "example2.csv"

# initializing the titles and rows list
fields = ['Index', 'Workorder ID', 'Description', 'Status', 'Type', 'Equipment Description', 'WO Owner', 'Priority', 'Scheduled Start Date', 'Scheduled End Date', 'PM Compliance Min Date', 'PM Compliance Max Date', 'Original PM due date', 'Completed date']
rows = []

def get_info():
	for row in rows[1:]:
		if row[6] == 'DEANEJST':
			print(row)
			# parsing each column of a row
			#for col in row:
				#	if col == 'DEANEJST':
				#print(col, end=" ")

# reading csv file
with open(filename, 'r') as csvfile:
	# creating a csv reader object
	csvreader = csv.reader(csvfile)
	
	# extracting field names through first row
	#fields = next(csvreader)

	# extracting each data row one by one
	for row in csvreader:
		rows.append(row)

	# get total number of rows
	print("Total no. of rows: %d"%(csvreader.line_num))

get_info()

#with open('fields.csv', 'w') as csvfile:
    # creating a csv writer object
#    csvwriter = csv.writer(csvfile)
    # writing the fields
#    csvwriter.writerow(fields)

#print(fields)



