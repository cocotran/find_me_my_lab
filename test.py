from scraper.scraper import *


URL = 'https://aits.encs.concordia.ca/assets/encs/html/Software%20for%20Windows%20in%20the%20Public%20Labs.html'
myScraper = Scraper(URL)
tags = myScraper.get_list_from_tag("tr", "td")

print(tags)