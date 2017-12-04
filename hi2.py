import sys
sys.path.insert(0, '/home/shreyansh/Desktop/smr/beautifulsoup4-4.4.1')

from bs4 import BeautifulSoup as BS
import urllib2
import csv

Url = sys.argv[1]
csvFileName = sys.argv[2]

def createData(url,csvfilename):
	fileName="hi.html"
	page =urllib2.urlopen(url)
	data=page.read()
	f = open(fileName,'w')
	f.write(data) # python will convert \n to os.linesep

	titleText=""
	isbn10Text=""
	isbn13Text=""
	priceText=""
	pageText=""
	authorText=""
	publisherText=""
	publicationYearText=""
	summaryText=""
	bookTypeText=""
	languageText=""


	with open(fileName, 'r') as myfile:
	    datatext=myfile.read().replace('\n', '')

	soup = BS(datatext,"lxml")

	title = soup.findAll('h1', {'class': 'title'})
	print "Title: ", title[0].text	

	titleText = title[0].text

	I = soup.findAll('td',{'class':'specsKey'})
	J = soup.findAll('td',{'class':'specsValue'})
	K= soup.find_all('div',{'class': 'price-wrap'})

	for i in range(0,len(I)) :
		if(I[i].text == "ISBN-10"):
			print "ISBN: ",J[i].text.strip()
			isbn10Text= J[i].text.strip()
		if(I[i].text == "ISBN-13"):
			print "ISBN-13: ", J[i].text.strip()
			isbn13Text = J[i].text.strip()
		if(I[i].text.strip() == "Number of Pages"):
			print "Pages: ", J[i].text.strip()
			pageText = J[i].text.strip()
		if(I[i].text.strip() == "Authored By"):
			print "author: ", J[i].text.strip()
			authorText = J[i].text.strip()
		if(I[i].text.strip() == "Publisher"):
			print "publisher: ", J[i].text.strip()
			publisherText = J[i].text.strip()
		if(I[i].text.strip() == "Publication Year"):
			print "publication Year: ", J[i].text.strip()
			publicationYearText = J[i].text.strip()
		if(I[i].text.strip() == "Binding"):
			print "binding: ", J[i].text.strip()
			bookTypeText = J[i].text.strip()
		if(I[i].text.strip() == "Language"):
			print "language: ", J[i].text.strip()
			languageText = J[i].text.strip()


	for tag in K:
	    tdTags = tag.find_all("span", {"class":"selling-price"})
	    for tag in tdTags:
	        print "price: ",tag.text
	        priceText = tag.text

	with open(csvfilename, 'a') as csvfile:
		writer = csv.writer(csvfile)
		#writer.writerow([titleText, isbn10Text,isbn13Text, priceText,pageText,authorText,publisherText,publicationYearText,summaryText,bookTypeText,languageText ])
		writer.writerow([titleText, isbn10Text,isbn13Text, priceText,pageText,authorText,publisherText,publicationYearText,bookTypeText,languageText ])
		#writer.writerow([titleText,  isbn10Text,isbn13Text, priceText, ])


createData(str(Url),str(csvFileName))

