from bs4 import BeautifulSoup
import requests
import re


req_url  = "http://www.productionparadise.com/search/index.php?t=members&country_id=&category_id=&q="
r  = requests.get(req_url)
data = r.text
soup = BeautifulSoup(data,'lxml')
pages = soup.find_all('div',{"class":"paginator"})
pages = str(pages)
pages = pages[pages.find('a class="nextprev"')-10:pages.find('a class="nextprev"')-1]
#print pages
# page = range(1,24)
# for i in page:
# 	print req_url + "&page=" + str(i)
# matchObj =  r'\>(.*?)\<'
# if re.search(matchObj, pages):
# 	print "as"
r  = requests.get(req_url)
data = r.text
soup = BeautifulSoup(data,'lxml')
for row in soup.find_all('div',attrs={"class" : "data"}):
	print row.text



	# data = row.text.splitlines()
	# print "\n\n\n\n\\n"
	# writer = Writer(row.text)
	# data = filter(None,data)
	# print type(data)
	# writer = Writer(data)
	# writer.get_name(data[0])
	# writer.get_phone(data[2])
	# try:
	# 	writer.get_website(data[4])
	# except IndexError:
	# 	writer.get_website(" ")

#print pages
