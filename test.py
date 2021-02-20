from scraper.scraper import *
from scraper.scraper_encs import *


database = scrape()
room_array = ["H811"]
room_data = list(database.keys())
result = {}
for i in range(len(room_data)):
    if room_data[i] in room_array:
        result[room_data[i]] = database[room_data[i]]

print(result)
