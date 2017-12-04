import urllib2

lines = [line.rstrip('\n') for line in open('ISBNbusiness.txt')]


for i in range(0,lines.length):
	url="https://www.goodreads.com/search?q=" + lines[i].strip()
	page =urllib2.urlopen(url)
	data=page.read()
	f = open('goodreads.html','w')
	f.write(data) # python will convert \n to os.linesep
	f.close()