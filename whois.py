from bs4 import BeautifulSoup
import requests
import json


BASE_URL = "http://api.whoapi.com/?domain="
APPEND_URL = "&r=whois&apikey="
API_KEY = "73328b9447e5dcfd4670c29332fa3bb1"

class WhoIsScraper(object):

    def get_raw_whois_data_api(self, company_url):
        """
            Gets raw whois data from BASE_URL + company name or company website.
            ....args:
            .........company_url: gives the domain that the company is registered with
        """
    
        REQUEST_URL = BASE_URL + company_url + APPEND_URL + API_KEY

        response = requests.get(REQUEST_URL)
        print("+++++++++++++++++++++++++")
        print(response)
        load_json = json.loads(response.text)
        if(not load_json['limit_hit']):
            print(load_json)
        else:
            print("Limit Hit")
    
    def get_raw_whois(self, company_url):
        """
            Gets raw whois data from BASE_URL + company name or company website.
            ....args:
            .........company_url: gives the domain that the company is registered with
        """

        BASE_URL = "https://www.whois.com/whois/"
        REQUEST_URL = BASE_URL + company_url
        print(REQUEST_URL)
        source = requests.get(REQUEST_URL)
        print(source)
        html_parse = BeautifulSoup(source.text, "html.parser")
        raw_find_data = html_parse.find("pre", {'id':'registryData'})
        # print(raw_find_data.text)

        raw_find_data = str(raw_find_data.text)
        print(raw_find_data)
            
            

w = WhoIsScraper()
w.get_raw_whois("claire.ai")