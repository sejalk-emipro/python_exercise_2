from bs4 import BeautifulSoup
from xml.dom import minidom

with open('5.xml', 'r') as f:
    data = f.read()
# Passing the stored data inside
# the beautifulsoup parser, storing
# the returned object
Bs_data = BeautifulSoup(data, "xml")
# Finding all instances of tag
# `unique`
template = Bs_data.find_all('template')
xpath = Bs_data.find_all('xpath')
link = Bs_data.find_all('link')
script = Bs_data.find_all('script')
for tag in template:
    print("Value of template tag Id attribute value :",tag["id"])
for tag in xpath:
    print("Value of xpath tag position attribute value :",tag["position"])
for tag in link:
    print("Value of link tag href attribute value :",list(tag["href"].split("/"))[-1])
for tag in script:
    print("Value of script tag src attribute value :",list(tag["src"].split("/"))[-1])
f.close()

# parse an xml file by name
file = minidom.parse('5.xml')

#use getElementsByTagName() to get tag
template = file.getElementsByTagName('template')
xpath = file.getElementsByTagName('xpath')
link = file.getElementsByTagName('link')
script = file.getElementsByTagName('script')
# all item attributes
print('\nAll attributes: Template')
for elem in template:
  print(elem.attributes['id'].value)
print('\nAll attributes: xpath')
for tag in xpath:
    print(tag.attributes['position'].value)
print('\nAll attributes: Link')
for tag in link:
    print(list(tag.attributes['href'].value.split("/"))[-1])
print('\nAll attributes: Script')
for tag in script:
    print(list(tag.attributes['src'].value.split("/"))[-1])


