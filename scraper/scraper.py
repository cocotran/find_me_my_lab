import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(
        self,
        url='https://aits.encs.concordia.ca/assets/encs/html/Software%20for%20Windows%20in%20the%20Public%20Labs.html'
    ) -> None:
        self.url = url

    def scrape(self) -> object:
        # Scrape HTML Content
        page = requests.get(self.url)
        # Parse HTML
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup

    def scrape(self, url: str) -> object:
        # Scrape HTML Content
        page = requests.get(url)
        # Parse HTML
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup

    def parse_by_HTML_tag(self, tag: str) -> object:
        soup = self.scrape(self.url)
        tags = soup.find_all(tag)
        return tags

    def get_list_from_tag(self, tag1: str, tag2: str) -> list:
        software_list = []
        for element in self.parse_by_HTML_tag(tag1):
            software_lab = [i.get_text() for i in element.find_all(tag2)]
            software_list.append(software_lab)
        return software_list
