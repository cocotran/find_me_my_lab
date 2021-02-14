import requests
from bs4 import BeautifulSoup

URL = 'https://aits.encs.concordia.ca/assets/encs/html/Software%20for%20Windows%20in%20the%20Public%20Labs.html'

# for element in rows:
#     software_lab = [i.get_text() for i in element.find_all('td')]
#     # TODO: add data to database

class Scraper:

    def __init__(self) -> None:
        pass

    def __init__(self, url) -> None:
        self.url = url

    def scrape(self) -> object:
        # Scrape HTML Content
        page = requests.get(self.url)
        # Parse HTML
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup

    def scrape(self, url) -> object:
        # Scrape HTML Content
        page = requests.get(url)
        # Parse HTML
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup

    def parse_by_HTML_tag(self, tag:str) -> object:
        soup = self.scrape()
        tags = soup.find_all(tag)
        return tags
