import sys
sys.path.insert(0, '/home/shreyansh/Desktop/smr/beautifulsoup4-4.4.1')

from bs4 import BeautifulSoup as BS
import urllib2
import csv

from os.path import basename


isbnFile = "second100.txt"
csvFileName =  "amazonList.csv"

ISBNs = [line.rstrip('\n') for line in open(isbnFile)]


for i in range(0,len(ISBNs)):
	print ISBNs[i]
	url="https://www.goodreads.com/search?q=" + ISBNs[i].strip()
	page =urllib2.urlopen(url)
	data=page.read()
	f = open('goodreadsToAmazon.html','w')
	f.write(data) 

	amazonLink=""

	with open('goodreadsToAmazon.html', 'r') as myfile:
		datatext=myfile.read().replace('\n', '')

	soup = BS(datatext,"lxml")

	try:
		amazonSoup = soup.findAll('a',{'id':'buyButton'})
		amazonLink = "www.goodreads.com" + amazonSoup[0]['href'].strip()
					
	except:
		pass

	with open(csvFileName, 'a') as csvfile:
			writer = csv.writer(csvfile)
			writer.writerow([ISBNs[i].strip(),amazonLink])

