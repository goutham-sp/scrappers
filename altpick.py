from bs4 import BeautifulSoup
import requests
import os
# import classify_name
# from first_last import names
# import excel
# from excel import Excel
# from classify_name import asdf
# from write_file import WriteOnFile


class AltPick:

	def __init__(self):
		self.links_dict = dict()
		self.count = 1
		self.c = 0
		self.loc = ''
		self.name = ''
		self.phone = ''
		self.link = ''
		self.websites = ''
		self.final_dict = dict()


	def get_next_url(self, URL):
		source = requests.get(URL)
		text_page = source.text
		bs = BeautifulSoup(text_page, "html.parser")
		is_end = bs.find('p', {'class' : 'accent'})
		is_end = is_end.string
		# print (is_end)
		if is_end == "No matches for your search.":
			print ('------------------')
		else:
			self.get_names_and_urls(URL)


	def get_names_and_urls(self, URL):
		source = requests.get(URL)
		text_page = source.text
		bs = BeautifulSoup(text_page, "html.parser")
		# print (is_end)
		for n in bs.findAll('span', {'class' : 'results_text'}):
			# print (type(n))
			n = str(n)
			# print (n)
			# cat = ""
			self.loc = ''
			# n[]
			self.link = n[n.find('<a href="'):n.find("</a>",1)]
			self.link = self.link[self.link.find("/"):self.link.find('">')]
			self.name = n[n.find('<a href="'):n.find("</a>",1)]
			self.name = self.name[self.name.find('">') + 2:self.name.find('</a>')]
			self.link = 'https://altpick.com' + self.link
			# cat = n[n.find('Genre: ') + len('Genre: '):n.find(']')]
			# cat = cat[cat.find('<br/>Genre: ') + len('<br/>Genre: '):n.find(', ',1)]
			self.loc = n[n.find('<br/>') + len('<br/>'):n.find('[',1)]
			print (str(self.count) + "  " + self.name + "\n" + self.link + '\n' + self.loc)
			self.count += 1
			self.links_dict.update({self.name:self.link})
		# print (self.links_dict)
		# print (self.final_dict)
		URL = URL + "&_ACT=search&offset=" + str(self.count)
		self.get_next_url(URL)
		# offset = bs.find('p' , {'class' : 'resultsNum'})
		# offset = offset.string


	def scrape_all(self, j):
			source = requests.get(j)
			text = source.text
			bs = BeautifulSoup(text, "html.parser")
			self.name = bs.find('font', {'class': 'bigHead'})
			self.name = self.name.string
			# name = name.string
			details = bs.find('table', {'class' : 'memberInfo'})
			self.phone = str(details)
			# print (self.phone)
			self.phone = self.phone[self.phone.find('<td><p>')+len('<td><p>'):self.phone.find(' (',1)]
			# phone = phone[phone.find('<p>'):phone.find(' (',1)]
			detail = str(details)
			exists = detail[detail.find('<p class="bold">Phone</p>'):]
			# print (exists)
			if exists == '<p class="bold">Phone</p>':
				self.phone = self.phone
			elif exists == '>':
				self.phone = ''
			print (self.phone)
			# address = details[details.find('<tr>')]
			self.websites = bs.find('table', {'cellpadding':'2'})
			self.websites = str(self.websites)
			self.websites = self.websites[self.websites.find('<p><a href="') + len('<p><a href="'):self.websites.find('" target="_blank">',1)]
			print (self.websites)


	def mainSpyder(self):
		for i,j in self.links_dict.items():
			self.scrape_all(j)
			self.final_dict.update({self.name:[self.loc, self.phone, self.link, self.websites]})
		print (self.final_dict)


def main():
	state = 'New York'
	URL = 'https://altpick.com/results?q=&genre=&city=&state=' + state + '&country=USA'
	n = AltPick()
	n.get_next_url(URL)
	n.mainSpyder()
	# dir_path = os.path.dirname(os.path.realpath(__file__))
	# try:
	# 	os.mkdir(dir_path + '\\' +state)
	# except WindowsError:
	# 	pass
	# dir_path1 = dir_path + "\\" + state
	# w = WriteOnFile(dir_path1, n.final_dict)
	# w.write_into_file()
	# asdf()
	# names()
	# exc = Excel(dir_path, state, 'suhas@claire.ai')
	# exc.execute()
	# exc.sendEmail()




if "__name__" is main():
	main()
