from bs4 import BeautifulSoup as bs4
import requests
import threading
import nltk


def get_company_about_page(company_link):

    """
        Gets and collects all the  about us links on a company's website
        ....args: 
        ........company_link: Company's website link
    """
    source = requests.get(company_link)
    source_bs4 = bs4(source.text, "html.parser")

    possible_links = list()
    possible_links.extend(list(link for link in source_bs4.findAll("a")))
    # print(possible_links)

    return possible_links


def search_for_about(possible_links):
    """
        Searches for the proper about us page on the company's website
        ....agrs:
        ........possible_links: A list of all the possible about us page
    """

    about_page = ""

    for link in possible_links:
        if link.text.lower() == 'about' or link.text.lower() == 'about us' or link.text.lower() == 'about-us':
            # print(link.text.lower())
            # print(str(link))
            about_page = str(link)
            about_page = about_page[about_page.find('href="') + len('href="'):about_page.find('">')]
            # print(about_page)
            break

    return about_page


def scrape_page(link):
    """
        Scrapes and gets major parts of the main page of the company's website that could possibily explains about the company
        ....args:
        ........link: Link to company's website
    """
    home_source = requests.get(link)
    print(home_source)
    home_source_bs4 = bs4(home_source.text, 'html.parser')
    # print(home_source_bs4)

    home_tokens = nltk.sent_tokenize(str(home_source_bs4))
    #print(home_tokens)
    document = list()

    other_docs_p = home_source_bs4.findAll("p")
    other_docs_h3 = home_source_bs4.findAll("h3")
    other_docs_h4 = home_source_bs4.findAll("h4")
    other_docs_h2 = home_source_bs4.findAll("h2")

    try:
        document.extend(list(other.text for other in other_docs_p))
        document.extend(list(other.text for other in other_docs_h2))
        document.extend(list(other.text for other in other_docs_h3))
        document.extend(list(other.text for other in other_docs_h4))
    except AttributeError:
        print("Can't find possible useful info")

    # print(document)

    return document


def main():
    document = list()
    document.extend(scrape_page("http://50.112.71.98"))
    # print(document)
    possible_links = get_company_about_page("http://50.112.71.98")
    about_page = search_for_about(possible_links)
    print(about_page)
    try:
        document.extend(scrape_page(about_page))
    except:
        pass
    print(document)



if __name__ == "__main__":
    main()
