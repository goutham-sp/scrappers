from bs4 import BeautifulSoup
import requests



class ProductHunt(object):

	def __init__(self):
		pass		


	def find_link(self, company_name):
		"""
			Find the link of the company name of the 
			....args:
			........company_name: String that specicifies the company name/website
		"""
			
		"""company_name.replace('.', '-')
		print(company_name)

		company_name.replace(" ", '-')
		print(company_name)

		company_name.replace("_", '-')
		print(company_name)"""

		potential_link_name = company_name
		link_to_page = "https://www.producthunt.com/posts/" + potential_link_name
		return link_to_page


	def scrape_product_page(self, link_to_page):
		"""
			Scrape data and tags from the producthunt.com page of the company
			....args:
			........link_to_page: A string with a link to the company's page on producthunt.com
		"""

		product_source = requests.get(link_to_page)
		print(product_source)
		product_source_bs4 = BeautifulSoup(product_source.text, 'html.parser')
			
		tags_found = product_source_bs4.findAll('span', {'class':'font_9d927 grey_bbe43 xSmall_1a46e normal_d2e66 topic_ca358 button_53e93 uppercase_a49b4'})
		print(tags_found)

		tags = list()
		for tag in tags_found:
			tag = str(tag.a)
			tag = tag[tag.find('" title="') + len('" title="'):tag.find('">')]
			print(tag)
			tags.append(tag)

		company_meta = product_source_bs4.find('h2', {'class':'font_9d927 grey_bbe43 small_231df normal_d2e66 headerPostTagline_98494'})
		print(company_meta.string)
		return_data = {'tags': tags, 'company_meta': company_meta.string}


def main():
	P = ProductHunt()
	link_to_page = P.find_link(company_name = "clarke-ai")
	tags_or_meta = P.scrape_product_page(link_to_page)


if __name__ == "__main__":
	main()