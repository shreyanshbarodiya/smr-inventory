import sys
sys.path.insert(0, '/home/shreyansh/Desktop/smr/beautifulsoup4-4.4.1')

from bs4 import BeautifulSoup as BS
import urllib2
import csv

from os.path import basename


isbnFile = "finalList.txt"
csvFileName =  basename(isbnFile) + "GoodreadsData.csv"

ISBNs = [line.rstrip('\n') for line in open(isbnFile)]


for i in range(0,len(ISBNs)):
	print ISBNs[i]
	url="https://www.goodreads.com/search?q=" + ISBNs[i].strip()
	page =urllib2.urlopen(url)
	data=page.read()
	f = open('goodreads.html','w')
	f.write(data) # python will convert \n to os.linesep

	summaryText=""
	titleText=""
	isbn10Text=""
	bindingTypeText=""
	pagesText=""

	with open('goodreads.html', 'r') as myfile:
		datatext=myfile.read().replace('\n', '')

	soup = BS(datatext,"lxml")

	titleSoup = soup.findAll('h1',{'id':'bookTitle'})
	titleText = titleSoup.text

	bindingSoup = soup.findAll('span',{'itemprop':'bookFormatType'})
	bindingTypeText = bindingSoup.text

	pagesSoup = soup.findAll('span',{'itemprop':'numberOfPages'})
	pagesText= pagesSoup.text

	A = soup.findAll('div',{'class':'infoBoxRowTitle'})
	B = soup.findAll('div',{'class':'infoBoxRowItem'})

	for i in range(0,len(I)) :
		if(A[i].text == "Original Title"):
			titleText= B[i].text.strip()
		if(A[i].text == "ISBN"):
			isbn10Text = B[i].text.strip()
		if(A[i].text == "Edition Language"):
			languageText = B[i].text.strip()

	K = soup.findAll('div',{'id':'description','class':['readable','stacked']})

	for tag in K:
		tdTags = tag.find_all("span", {"style":"display:none"})
		for tag in tdTags:
		    #print "summary: ",tag.text , "\n"
		    summaryText=tag.text.encode('utf-8')

	authorText=""
	L = soup.findAll('div',{'id':'bookAuthors'})
	
	for tag in L:
		tdTags = tag.find_all("span", {"itemprop":"name"})
		for tag in tdTags:
		    #print "summary: ",tag.text , "\n"
		    authorText=tag.text.encode('utf-8')

	M = soup.findAll('a',{"class":['bookPageGenreLink']})

	try:
		a1 = M[0].text
		a2 = M[2].text
		a3 = M[4].text
	except:
		a1=""
		a2=""
		a3=""

	with open(csvFileName, 'a') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow([titleText, isbn10Text, ISBNs[i].strip(),"Rs. ---", pagesText,"publication", "publicationYear",bindingTypeText,languageText,authorText,a1,a2,a3, summaryText])
		#writer.writerow([titleText,  isbn10Text,isbn13Text, priceText, ])

