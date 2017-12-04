import sys
sys.path.insert(0, '/home/shreyansh/Desktop/smr/beautifulsoup4-4.4.1')

from bs4 import BeautifulSoup as BS
import urllib2
import urllib
import csv


imageFolder =  "ImagesISBN/"

isbnFile = "finalList.txt"

ISBNs = [line.rstrip('\n') for line in open(isbnFile)]


def saveImage(Url,isbn):
	fileName="images.html"
	page =urllib2.urlopen(Url)
	data=page.read()
	f = open(fileName,'w')
	f.write(data)

	with open(fileName, 'r') as myfile:
	    datatext=myfile.read().replace('\n', '')

	soup = BS(datatext,"lxml")

	I = soup.findAll('img',{'id':'coverImage'})
	
	imageUrlText = I[0].text

	filename = isbn + ".jpeg"
	urllib.urlretrieve(imageUrlText, filename )


for i in range(0,len(ISBNs)):
	url="https://www.goodreads.com/search?q=" + ISBNs[i].strip()
	saveImage(str(url),ISBNs[i])
