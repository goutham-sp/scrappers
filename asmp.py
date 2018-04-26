from bs4 import BeautifulSoup
import requests
import os
# import classify_name
# from first_last import names
# import excel
# from excel import Excel
# from classify_name import asdf
# from write_file import WriteOnFile


class MainClass(object):

	def __init__(self, state):
		self.links_Dict = dict()
		self.final_Dict = dict()
		dir_path = os.path.dirname(os.path.realpath(__file__))
		try:
			os.mkdir(dir_path + '\\' + state)
		except WindowsError:
			pass

		os.chdir(dir_path + '\\' + state)


	def scrape_this_page(self):
		for name,link in self.links_Dict.iteritems():
			source = requests.get(link)
			# print (source)
			text = source.text
			spl = ''
			p = re.compile(r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})")
			w = re.compile(r"((?:https\:\/\/)|(?:http\:\/\/)|(?:www\.))?([a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}(?:\??)[a-zA-Z0-9\-\._\?\,\'\/\\\+&%\$#\=~]+)")
			#### Change the regex in e #####
			e = re.compile(r"([\w\.\-_]+)?\w+@[\w-_]+(\.\w+){1,}")
			################################
			# print (text)
			bs = BeautifulSoup(text,"html.parser")
			for par in bs.findAll('h1',{'class':'faph-portfolio__title'}):
				name = par.string
				print (name)
			for det in bs.findAll('ul',{'class':'faph-portfolio__details'}):
				det = str(det)
				# print (det)
				loc = det[det.find('Address:</b>')+len('Address:</b>'):det.find('</li>',1)]
				loc = loc.split()
				for l in loc:
					if int(l) in range(48,57) or int(l) in range(65,90) or int(l) in range(97,122) or int(l) is 35 or int(l) is 32:
						loc1 = loc1 + l
					else:
						pass
				print (loc1)
				phn = p.findall(det)
				for i in phn:
					if len(i) >= 12:
						phn = i
				print (phn)
				web = w.findall(det)
				web = web[0]
				web = web[0] + web[1]
				print (web)
				eml = e.findall(det)
				print (eml)
				spl = det[det.find('Specialties:</b>')+len('Specialties:</b>'):spl.find('</li>',1)]
				spl = spl[spl.find('                  ')+len('                  '):spl.find(', ')]
				print (spl)
			self.final_Dict.update({name:[loc1,phn,web,eml,spl]})


	def mainSpyder(self, URL):
		source = requests.get(URL)
		text = source.text
		URL = 'none'
		bs = BeautifulSoup(text,"html.parser")
		for name in bs.findAll('h2',{'class':'post-title'}):
			name = str(name)
			print ('-------------')
			name1 = name[name.find('" title="'):name.find('</a>',1)]
			name1 = name1[name1.find('" title="')+len('" title="'):name1.find('">',1)]
			link = name[name.find('<a href="') + len('<a href="'):name.find('" title="',1)]
			print (name1)
			print (link)
			self.links_Dict.update({name1:link})
		for next_Link in bs.findAll('a',{'class':'next page-numbers'}):
			next_Link = 'https://asmp.org' + next_Link.get('href')
			URL = next_Link
		return URL


	def write_into_file(self):
		with open("TestaA-3.txt", 'ab') as file:
			for i,j in self.final_dict.iteritems():
				i = str(i)
				file.write(i + "\n")

		with open("TestbB-3.txt", 'ab') as file:
			for i,j in self.final_dict.iteritems():
				k = j[4]
				file.write(k + "\n")

		with open("TestcC-3.txt", 'ab') as file:
			for i,j in self.final_dict.iteritems():
				k = j[0]
				file.write(k + "\n")

		with open("TestdD-3.txt", 'ab') as file:
			for i,j in self.final_dict.iteritems():
				k = j[1]
				file.write(k + "\n")

		with open("TesteE-3.txt", 'ab') as file:
			for i,j in self.final_dict.iteritems():
				k = j[3]

		with open("TestfF-3.txt", 'ab') as file:
			for i,j in self.final_dict.iteritems():
				k = str(j[2])
				file.write(k + "\n")



def main():
	state = "New York"
	www = MainClass(state)
	URL = "https://www.asmp.org/find-a-photographer/?gmw_address%5B0%5D=" + state + "&gmw_distance=200&gmw_faph_name&gmw_faph_sort=distance&gmw_faph_view=card&gmw_form=1&gmw_per_page=50&gmw_lat&gmw_lng&gmw_px=pt&action=gmw_post"
	while URL is not 'none':
		URL = www.mainSpyder(URL)
	www.scrape_this_page()

if "__name__" is main():
	main()
