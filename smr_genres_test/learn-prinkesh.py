import csv

csvFileName = "output.csv"

testArray = [ [1,2,3], [4,5,6], [7,8,9] ]

with open(csvFileName, 'a') as csvfile:
	writer = csv.writer(csvfile)
	for row in testArray:
		writer.writerow(row)
