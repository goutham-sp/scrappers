import requests
import json
import re


class WikipediaScraper(object):

    def __init__(self):
        pass

    
    def get_response(self, company_name):
        """
            Gets and parses the response from wikipedia with error handling
            ....args:
            ........company_name: String which specifies the name of the company
        """
        request_url = "https://en.wikipedia.org/w/api.php?action=query&titles="+ company_name +"&prop=revisions&rvprop=content&format=json"
        print(request_url)
        wiki_response = requests.get(request_url)
        print(wiki_response)
        wiki_response_json = json.loads(wiki_response.text)
        # print(wiki_response_json)
        wiki_query = wiki_response_json['query']
        wiki_query_pages = wiki_query['pages']

        if str(wiki_response) == "<Response [404]>":
            print("404 Error")
            return None
        else:
            print("Page Found")
            return wiki_query_pages
        
        
    def parse_response(self, wiki_response):
        """
        ....args:
        ........wiki_response: Dictionary that contains the pages
        """
        wiki_pages_revisions = list()

        # print(wiki_response)
        for page in wiki_response:
            print(page)
            wiki_pages_revisions = wiki_response[page]['revisions']

        wiki_star = ""
        for item in wiki_pages_revisions:
            wiki_star = item['*']
            print(wiki_star)

        return wiki_star

        
            


def main():
    z = WikipediaScraper()
    h = z.get_response("Apple Inc.")
    z.parse_response(h)
    # print(h)


if __name__ == "__main__":
    main()