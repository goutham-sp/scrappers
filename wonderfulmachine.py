import requests
from fuzzywuzzy import fuzz
from bs4 import BeautifulSoup
import os
# import classify_name
# from first_last import names
# import excel
# from excel import Excel
# from classify_name import asdf
# from write_file import WriteOnFile as put
# # from multiprocessing import Queue
import threading


class WonderfulMachine:

	def __init__(self):
		self.NAME = 'none'
		self.PHONE = 'none'
		self.LOCATION = 'none'
		self.SPECIALITY = 'none'
		self.WEBSITE = 'none'
		self.EMAIL = 'none'
		self.REQUESTED_LOCATION = 'none'
		self.name_list = list()
		self.href_list = list()
		# print "Here"
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		try:
			str_loc = '\\' + str(self.REQUESTED_LOCATION)
			os.mkdir(self.dir_path + str_loc)
		except (OSError, IOError):
			pass
		os.chdir(self.dir_path + str_loc + '\\')
		self.dir_path = os.path.dirname(os.path.realpath(__file__))


	def photographer_page_spyder(self, URL):
		source = requests.get(URL)
		print ("--------------\n")
		print (source)
		text = source.text
		bs = BeautifulSoup(text, "html.parser")
		# p1 = put(self.dir_path)
		for l in bs.findAll('div', {'class' : 'photographer photographer--meta'}):
			self.LOCATION = l.string
			if self.REQUESTED_LOCATION is '' or self.REQUESTED_LOCATION is 'none':
				self.REQUESTED_LOCATION = self.LOCATION
		if fuzz.ratio(self.REQUESTED_LOCATION, self.LOCATION) > 50:
			# print (LOCATION)
			for n in bs.findAll('a', {'class' : 'photographer--name-link photographer--website'}):
				self.NAME = n.string
				print (self.NAME)
			for p in bs.findAll('a', {'class' : 'photographer-contact--link photographer--phone'}):
				self.PHONE = p.string
				print (self.PHONE)
			print (self.LOCATION)
			for s in bs.findAll('a', {'class' : 'js-spec--toggle photographer--specialty-list-link current'}):
				self.SPECIALITY = s.string
				print (self.SPECIALITY)
			for w in bs.findAll('a', {'class' : 'photographer-contact--link photographer--website'}):
				self.WEBSITE = w.string
				print (self.WEBSITE)
			for e in bs.findAll('a', {'class' : 'photographer-contact--link photographer--email'}):
				self.EMAIL = e.string
				print (self.EMAIL)
		p1.write_into_file('TestdD-3.txt', self.PHONE)
		p1.write_into_file('TestaA-3.txt', self.NAME)
		p1.write_into_file('TestfF-3.txt', self.WEBSITE)
		p1.write_into_file('TestbB-3.txt', self.SPECIALITY)
		p1.write_into_file('TestcC-3.txt', self.LOCATION)
		p1.write_into_file('TesteE-3.txt', self.EMAIL)


	def next_parser(self, URL):
		source = requests.get(URL)
		text = source.text
		href = []
		bs = BeautifulSoup(text, "html.parser")
		for j in bs.findAll('a', {'class' : 'pagination--next pagination-page-link active'}):
			href.append(j.get('href'))
		self.find_sidebar_links(href)


	def find_sidebar_links(self, URL):
			source = requests.get(URL)
			text = source.text
			bs = BeautifulSoup(text, "html.parser")
			for l in bs.findAll('span', {'class' : 'photographer--name'}):
				if l.string in self.name_list:
					pass
				else:
					self.name_list.append(l.string)
					print (l.string)
					for i in bs.findAll('span', {'class' : 'photographer--location'}):
						# print (i.string)
						self.LOCATION = i.string
						if self.REQUESTED_LOCATION is '' or self.REQUESTED_LOCATION is 'none':
							self.REQUESTED_LOCATION = self.LOCATION
					if fuzz.ratio(self.REQUESTED_LOCATION, self.LOCATION) > 50:
						for j in bs1.findAll('a', {'class' : 'photographer-list--link'}):
							href_new = 'http://wonderfulmachine.com' + j.get('href')
							print (href_new)
							self.href_list.append(href_new)

			self.next_parser(URL)


	def main_spyder(self, START_URL):
		main_page_list = list()
		source = requests.get(START_URL)
		text = source.text
		print ('Running')
		bs = BeautifulSoup(text, "html.parser")
		for j in bs.findAll('span', {'class' : 'photographer--name'}):
			if j.string in self.name_list:
				pass
			else:
				self.name_list.append(j.string)
				print (j.string)
				for i in bs.findAll('a',{'class' : 'photographer-list--link'}):
					href_new = 'https://wonderfulmachine.com' + i.get('href')
					main_page_list.append(href_new)
					self.href_list = main_page_list
					print (href_new)
					# print 'Still Running!!!'
					# print i
					t1 = threading.Thread(target = self.find_sidebar_links, args = (href_new,))
					# t1.daemon = True
					t1.start()
					# t1.join()
					# print self.href_list
					# print j

		for link in self.href_list:
			t2 = threading.Thread(target = self.photographer_page_spyder, args = (link,))
			# t2.daemon = True
			t2.start()
			# t2.join()


def main():
	dir_path = os.path.dirname(os.path.realpath(__file__))
	www = WonderfulMachine()
	print ('start')
	www.main_spyder('https://wonderfulmachine.com/find-photographers')
	print ('spyder_done')
	# exc = Excel(dir_path, www.REQUESTED_LOCATION, 'gouth96@gmail.com')
	# asdf()
	# print '\n***************\n\n'
	# names()
	# print '\n***************\n\n'
	# exc.execute()
	# print '\n***************\n\n'
	# exc.sendEmail()
	# print '\nMail sent!\n\n'


if "__name__" is main():
	main()
