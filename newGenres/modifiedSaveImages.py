import sys
sys.path.insert(0, '/home/shreyansh/Desktop/smr/beautifulsoup4-4.4.1')

from bs4 import BeautifulSoup as BS
import urllib2
import urllib
import csv

Url = sys.argv[1]
imageFolder = sys.argv[2].strip() + "ImagesISBN/"


def saveImage(url):
	fileName="images.html"
	page =urllib2.urlopen(url)
	data=page.read()
	f = open(fileName,'w')
	f.write(data)

	with open(fileName, 'r') as myfile:
	    datatext=myfile.read().replace('\n', '')

	soup = BS(datatext,"lxml")

	I = soup.findAll('td',{'class':'specsKey'})
	J = soup.findAll('td',{'class':'specsValue'})

	for i in range(0,len(I)) :
		if(I[i].text == "ISBN-13"):
#			print "ISBN-13: ", J[i].text.strip()
			isbn13Text = J[i].text.strip()

	imageUrl = soup.findAll('img',{'class' : ['productImage','current']})

	imageUrlText = imageUrl[0]['data-src']
#	print imageUrl[0]['data-src']

	filename = imageFolder + isbn13Text + ".jpeg"
	urllib.urlretrieve(imageUrlText, filename )



saveImage(str(Url))

#print Url
#print imageFolder
