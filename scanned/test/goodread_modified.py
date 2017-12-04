import sys
sys.path.insert(0, '/home/shreyansh/Desktop/smr/beautifulsoup4-4.4.1')

from bs4 import BeautifulSoup as BS
import urllib2
import csv

from os.path import basename


isbnFile = "isbns.txt"
csvFileName =  "genres.csv"

ISBNs = [line.rstrip('\n') for line in open(isbnFile)]

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

for i in range(0,len(ISBNs)):
	print ISBNs[i]
	url="https://www.goodreads.com/search?q=" + ISBNs[i].strip()
	page =urllib2.urlopen(url)
	data=page.read()
	f = open('goodreads.html','w')
	f.write(data) # python will convert \n to os.linesep

	# summaryText=""
	# titleText=""
	# isbn10Text=""
	# bindingTypeText=""
	# pagesText=""
	# authorText=""

	with open('goodreads.html', 'r') as myfile:
		datatext=myfile.read().replace('\n', '')

	soup = BS(datatext,"lxml")

#	try:
		# titleSoup = soup.findAll('h1',{'id':'bookTitle'})
		# titleText = titleSoup[0].text.encode('utf-8')

		# bindingSoup = soup.findAll('span',{'itemprop':'bookFormatType'})
		# bindingTypeText = bindingSoup[0].text.encode('utf-8')

		# pagesSoup = soup.findAll('span',{'itemprop':'numberOfPages'})
		# pagesText= pagesSoup[0].text.encode('utf-8')

		# A = soup.findAll('div',{'class':'infoBoxRowTitle'})
		# B = soup.findAll('div',{'class':'infoBoxRowItem'})

		# for it in range(0,len(A)) :
		# 	if(A[it].text == "Original Title"):
		# 		titleText= B[it].text.strip().encode('utf-8')
		# 	if(A[it].text.strip() == "ISBN"):
		# 		isbn10Text = B[it].text.strip().encode('utf-8')
		# 	if(A[it].text == "Edition Language"):
		# 		languageText = B[it].text.strip().encode('utf-8')

		# K = soup.findAll('div',{'id':'description','class':['readable','stacked']})

		# for tag in K:
		# 	tdTags = tag.find_all("span", {"style":"display:none"})
		# 	for tag in tdTags:
		# 	    summaryText=tag.text.encode('utf-8').encode('utf-8')


		# L = soup.findAll('div',{'id':'bookAuthors'})
		
		# for tag in L:
		# 	tdTags = tag.find_all("span", {"itemprop":"name"})
		# 	for tag in tdTags:
		# 	    authorText=tag.text.encode('utf-8')
#	except:
#		pass


	mList = []
	try:
		M = soup.findAll('a',{"class":['bookPageGenreLink']})
		for j in range(0,len(M)):
			g = M[j].text.encode('utf-8')
			if (hasNumbers(g)):
				#print g
				continue
			else:
				mList.append(g)
		# a1 = M[0].text.encode('utf-8')
		# a2 = M[2].text.encode('utf-8')
		# a3 = M[4].text.encode('utf-8')
	except:
		pass

	# for k in range(0,len(mList)):
	# 	print mList[k]

	with open(csvFileName, 'w') as csvfile:
		writer = csv.writer(csvfile)
		#nRow.extend(mList)
		mList.insert(0,ISBNs[i])
		if(len(mList)==1):
			print "no genres found"
			writer.writerow(mList)
		else:
			print str(len(mList)) + " genres found"
			writer.writerow(mList)

