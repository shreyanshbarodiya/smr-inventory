from HTMLParser import HTMLParser

pstring = source_code = """<span class="UserName"><a href="#">Martin<span> Elias</span></a></span>"""


class myhtmlparser(HTMLParser):
    def __init__(self):
        self.reset()
        self.NEWTAGS = []
        self.NEWATTRS = []
        self.HTMLDATA = []
    def handle_starttag(self, tag, attrs):
        self.NEWTAGS.append(tag)
        self.NEWATTRS.append(attrs)
    def handle_data(self, data):
        self.HTMLDATA.append(data)
    def clean(self):
        self.NEWTAGS = []
        self.NEWATTRS = []
        self.HTMLDATA = []

parser = myhtmlparser()

with open('hi.html', 'r') as myfile:
    datatext=myfile.read().replace('\n', '')
#parser.feed(datatext)
parser.feed(pstring)
# Extract data from parser
tags  = parser.NEWTAGS
attrs = parser.NEWATTRS
data  = parser.HTMLDATA

# Clean the parser
parser.clean()

# Print out our data
print tags
print attrs
print data

print len(tags)


#if(attrs[0][0][0]=='class'):
#    print attrs[0][0][1]