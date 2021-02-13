import requests
from bs4 import BeautifulSoup

URL = 'https://aits.encs.concordia.ca/assets/encs/html/Software%20for%20Windows%20in%20the%20Public%20Labs.html'

# Scrape HTML Content
page = requests.get(URL)

# Parse HTML
soup = BeautifulSoup(page.content, 'html.parser')

# Parse each row of software - lab rooms
rows = soup.find_all('tr')

for element in rows:
    software_lab = [i.get_text() for i in element.find_all('td')]
    # TODO: add data to database