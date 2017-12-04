import sys
sys.path.insert(0, '/home/shreyansh/Desktop/smr/beautifulsoup4-4.4.1')

from bs4 import BeautifulSoup as BS
import urllib2
import urllib
import csv

Url = sys.argv[1]
Count = sys.argv[2]
imageFolder = sys.argv[3]


def saveImage(url,count):
	fileName="images.html"
	page =urllib2.urlopen(url)
	data=page.read()
	f = open(fileName,'w')
	f.write(data) # python will convert \n to os.linesep


	with open(fileName, 'r') as myfile:
	    datatext=myfile.read().replace('\n', '')

	soup = BS(datatext,"lxml")

	# title = soup.findAll('h1', {'class': 'title'})
	# print "Title: ", title[0].text	

	imageUrl = soup.findAll('img',{'class' : ['productImage','current']})

	imageUrlText = imageUrl[0]['data-src']
	print imageUrl[0]['data-src']

	filename = imageFolder + count + ".jpeg"
	urllib.urlretrieve(imageUrlText, filename )



saveImage(str(Url),Count)

