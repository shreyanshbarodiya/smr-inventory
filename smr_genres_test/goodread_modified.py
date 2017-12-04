import sys
sys.path.insert(0, '/home/shreyansh/Desktop/smr/beautifulsoup4-4.4.1')

from bs4 import BeautifulSoup as BS
import urllib2
import csv

from os.path import basename


isbnFile = "isbns.txt"
csvFileName =  "genres_2.csv"

ISBNs = [line.rstrip('\n') for line in open(isbnFile)]

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

for i in range(470,485):
	print ISBNs[i]
	url="https://www.goodreads.com/search?q=" + ISBNs[i].strip()
	page =urllib2.urlopen(url)
	data=page.read()
	f = open('goodreads.html','w')
	f.write(data) # python will convert \n to os.linesep

	with open('goodreads.html', 'r') as myfile:
		datatext=myfile.read().replace('\n', '')

	soup = BS(datatext,"lxml")



	mList = []
	try:
		M = soup.findAll('a',{"class":['bookPageGenreLink']})
		for j in range(0,len(M)):
			g = M[j].text.encode('utf-8')
			if (hasNumbers(g)):
				continue
			else:
				mList.append(g)
	except:
		pass


	with open(csvFileName, 'a') as csvfile:
		writer = csv.writer(csvfile)
		mList.insert(0,ISBNs[i].strip())
		if(len(mList)==1):
			print "no genres found"
			writer.writerow(mList)
		else:
			print str(len(mList)) + " genres found"
			writer.writerow(mList)

