import sys
sys.path.insert(0, '/home/shreyansh/Desktop/smr/beautifulsoup4-4.4.1')

from bs4 import BeautifulSoup as BS
import urllib2
import csv
import re
from os.path import basename


amazonLinks = "amazonLinks"
csvFileName =  "amazonData.csv"

links = [line.rstrip('\n') for line in open(amazonLinks)]



def fetchDataFromAmazon(url):

	paperbackText = ""
	publisherText = ""
	languageText = ""
	isbn10Text = ""
	isbn13Text = ""
	mrpText= ""
	datatext=""

	url = "http://" + str(url)

	try:
		opener = urllib2.build_opener()
		opener.addheaders = [('User-agent', 'Mozilla/10.0')]
		response = opener.open(url)
		html_contents = response.read()
		f = open('amazon.html','w')
		f.write(html_contents) 

		with open('amazon.html', 'r') as myfile:
			datatext=myfile.read().replace('\n', '')
	except:
		pass

	soup = BS(datatext,"lxml")

	print url

	A = soup.findAll('td',{'class':'bucket'})
	mrpSoup = soup.findAll('span',{'class': 'a-text-strike' })
	try:
		mrpText = mrpSoup[0].text.encode('utf-8')
	except:
		pass
		
	for tag in A:
		liTags = tag.find_all("li")
		for tag in liTags:
			temp = tag.text
			temp2 = re.split(r'\:|\n', temp)
			key =  temp2[0].strip()
			# if(key == "ISBN-13"):
			# 	isbn13Text = temp2[1].strip()
			# 	print isbn13Text	
			try:
				if(key == "Paperback"):
					paperbackText = temp2[1].strip()
			except:
				pass
			
			try:
				if(key == "Publisher"):
					publisherText = temp2[1].strip()	
			except:
				pass
			
			try: 
				if(key == "Language"):
					languageText = temp2[1].strip()	
			except:
				pass

			try:
				if(key == "ISBN-10"):
					isbn10Text = temp2[1].strip()	
			except:
				pass
			try:	
				if(key == "ISBN-13"):
					isbn13Text = temp2[1].strip()	
			except:
				pass

	with open(csvFileName, 'a') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow([ isbn10Text, isbn13Text, paperbackText ,mrpText,publisherText, languageText ])


#Uncomment this 
for i in range(0, len(links)):
	#print links[i]
	fetchDataFromAmazon(links[i])

# #comment the following
# for i in range(0, 15):
# 	fetchDataFromAmazon(links[i])
