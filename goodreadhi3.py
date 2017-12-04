import sys
sys.path.insert(0, '/home/shreyansh/Desktop/smr/beautifulsoup4-4.4.1')

from bs4 import BeautifulSoup as BS
import urllib2
import csv

from os.path import basename




isbnFile = sys.argv[1]
csvFileName =  basename(isbnFile) + "GoodreadsData.csv"

ISBNs = [line.rstrip('\n') for line in open(isbnFile)]


for i in range(0,len(ISBNs)):
	url="https://www.goodreads.com/search?q=" + ISBNs[i].strip()
	page =urllib2.urlopen(url)
	data=page.read()
	f = open('goodreads.html','w')
	f.write(data) # python will convert \n to os.linesep

	summaryText=""
	with open('goodreads.html', 'r') as myfile:
		datatext=myfile.read().replace('\n', '')

	soup = BS(datatext,"lxml")

	K = soup.findAll('div',{'id':'description','class':['readable','stacked']})
	#print len(K)
	for tag in K:
		tdTags = tag.find_all("span", {"style":"display:none"})
		for tag in tdTags:
		    print "summary: ",tag.text , "\n"
		    summaryText=tag.text.encode('utf-8')

	with open(csvFileName, 'a') as csvfile:
		writer = csv.writer(csvfile)
		#writer.writerow([titleText, isbn10Text,isbn13Text, priceText,pageText,authorText,publisherText,publicationYearText,summaryText,bookTypeText,languageText ])
		writer.writerow([ISBNs[i].strip(),summaryText])
		#writer.writerow([titleText,  isbn10Text,isbn13Text, priceText, ])

