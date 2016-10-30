# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

links = list()
lst = list()

url = raw_input("Enter a URL: ")
position = raw_input("Enter Position: ")
position = int(position)
count = raw_input("Enter count: ")
count = int(count)


while count>0:
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	
	tags = soup('a')
	for tag in tags:
		links.append(tag.get('href', None))
		lst.append(tag.contents[0])
	url= links[position-1]	
	name = str(lst[position-1])
	count = count - 1
	links = []
	lst = []
print name

