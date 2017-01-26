#!/usr/bin/python

################
## Word finder - leveraging off the urllib2 & Bbeautiful Soup module
## Simple command-line tool to lookup words and provide
# dictionary / thesaurus functionality.
################

import urllib2, string, pprint
from BeautifulSoup import BeautifulSoup

word = raw_input("Enter word: ")
url = "http://www.dictionary.com/browse/" + word
hits = [] 
definitions = {}

soup = BeautifulSoup(urllib2.urlopen(url).read())
for hit in soup.findAll('div',attrs={'class' : 'def-content'}):
    text = str(hit.contents[0].strip())
    text = pprint.pformat(text)
    hits.append(text)

for i in hits:
    if i == "''":
        hits.remove(i)
    if i == "'('":
        hits.remove(i)

for i in hits:
    print pprint.pformat(i)

#to be continued...
