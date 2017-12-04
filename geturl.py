# import sys
# import pycurl

# class ContentCallback:
#         def __init__(self):
#                 self.contents = ''

#         def content_callback(self, buf):
#                 self.contents = self.contents + buf

# t = ContentCallback()
# curlObj = pycurl.Curl()
# curlObj.setopt(curlObj.URL, 'http://www.google.com')
# curlObj.setopt(curlObj.WRITEFUNCTION, t.content_callback)
# curlObj.perform()
# curlObj.close()
# print( t.contents)

import urllib2
url="https://www.googleapis.com/books/v1/volumes?q=isbn:1780221355"
page =urllib2.urlopen(url)
data=page.read()
f = open('new.json','w')
f.write(data) # python will convert \n to os.linesep
f.close()