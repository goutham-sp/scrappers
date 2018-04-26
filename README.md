# scrappers

word2vec scrapers:

	w2v_scraper.py: Scrapes data off sense2vec output trained with reddit dataset
		Scrapes data off https://explosion.ai/demos/sense2vec.
		The model that is used is trained is up-to-date. Scraping off of this is more accurate than the library.
  
	w2v_scraper_gnews.py: Scrapes data off sense2vec output trained with google news dataset
		Scrapes data off https://rare-technologies.com/word2vec-tutorial/
		The model used is trained with google news dataset.

	altpick.py : Scrapes data of photographers of specific location
		https://altpick.com/ is the source website.
	
	asmp.py : Scrapes data of photographers of specific location
		hhtps://asmp.org/ is the source website
		
	wonderfulmachine.py : Scrapes data of photographers of specific location
		https://wonderfulmachines.com/ is the source website
	
	production_paradise.py : Scrapes data of photographers of specific location
		https://www.productionparadise.com/ is the source website
		
	company_page.py : Scrapes all useful information from a company's website
		Any page with important info can be scraped
	
	producthunt.py : Scrapes data about a company from https://producthunt.com
	
	whois.py : Scrapes data from whois website for specified company website
	
	wiki.py : Looks up about a company on wikipedia
