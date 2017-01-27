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


print "\n Definitions -  \n"

for i in hits:
    if i == "'('":
        continue #i = i.replace("(", "")
    if i == "''":
        continue #i = i.replace("''", '')
    print "\n" + pprint.pformat(i)


prompt = raw_input("\n Synonyms? Please enter y/n: ")

if prompt == 'n':
    exit()

thesaurus_url = 'http://www.thesaurus.com/browse/' + word

soup_two = BeautifulSoup(urllib2.urlopen(thesaurus_url).read())
for hit in soup_two.findAll('span', attrs={'class' : 'text'}):
    text = str(hit.contents[0].strip())
    text = pprint.pformat(text)
    hits.append(text)
    print '\n' + text 

