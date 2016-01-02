# from mako.template import Template
#


# mytemplate = Template(filename='/Users/hongle/Dropbox/cs297/codecheckXblock/README.txt')
# print(mytemplate.render())

# tutorial:  http://chrisalbon.com/python/beautiful_soup_html_basics.html
# beautiful soup example
import urllib2
from bs4 import BeautifulSoup, Comment
# link with 1 box answer
r = urllib2.urlopen(url= "http://codecheck.it/codecheck/files?repo=bj4fp&problem=ch04/c04_exp_4_7")

# link with more than 1 boxes answer
#r = urllib2.urlopen(url='http://codecheck.it/codecheck/files?repo=bj4fp&problem=ch04/c04_exp_4_7').read()
# get the website source
b = BeautifulSoup(r, "html.parser")
url = 'http://codecheck.it/codecheck/files?repo=bj4cc&problem=ch02/c02_exp_2_102'
r1 = urllib2.urlopen(url)
b1 = BeautifulSoup(r1, "html.parser")
#get all content for the website
#
# b3 = b1.find_all("form")
# count = 0
# a = None
# for box in b3[0].find_all("textarea"):
#     #get info from the box
#     count += 1
#     a= box.get_text()
#
#
# print a
#

#print count


#for box in b3.find_all("textarea"):

#a = str(b.find_all('form')[0]).replace('/codecheck/check','http://codecheck.it/codecheck/check')
#print a
#for box in b.find_all("textarea"):
 #   print box.get_text()

# print out the entire website in structure tree
#print(b.prettify())
# print paragraph out

#print(b1.p.text)
#print(b1.pre.text)
a = ""
a = b1.pre.text
print a.replace('\n', '<br />')
#get all paragraph in web


#print out the question text
#print b.pre.text

# get the paragraph id
# paras = b.findAll('p', recursive=True)
# for i, p in enumerate(paras):
#     p['id'] = "p%s" % i

# print out the second paragraph
#print b.find_all('p')[1]
# or this way
#secondP = b.find("p").findNext("p").get_text()
#print secondP

#print out more than 1 form
#formP = b.find("form", attrs={ "method" : "post" })
#for i in formP:
#    print i