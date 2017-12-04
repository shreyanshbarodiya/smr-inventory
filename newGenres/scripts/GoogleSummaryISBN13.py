import sys
sys.path.insert(0, '/home/shreyansh/Desktop/smr/beautifulsoup4-4.4.1')

from bs4 import BeautifulSoup as BS
import urllib2
import csv

import json
from pprint import pprint

isbnFileName = sys.argv[1]
csvFileName = sys.argv[2]

lines = [line.rstrip('\n') for line in open(str(isbnFileName))]


for i in range(0,len(lines)):

	data="{}"
	try:
		url="https://www.googleapis.com/books/v1/volumes?q=isbn:" + lines[i].strip() + "&key=AIzaSyCWGvXIirIU42CQD3wcbSbRFRiUjdKIwrI"
		page =urllib2.urlopen(url)
		data=page.read()
	except:
		pass

	f = open('book.json','w')
	f.write(data) # python will convert \n to os.linesep
	f.close()

	description=""
	with open('book.json') as data_file:
	    jsonData = json.loads(data_file.read())


	try:
		description = str(jsonData["items"][0]["volumeInfo"]["description"])

		
	except: 
		pass

	with open(str(csvFileName), 'a') as csvfile:
				writer = csv.writer(csvfile)
				writer.writerow([lines[i],description])
