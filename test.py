from scraper.scraper import *
from scraper.scraper_encs import *


database = scrape()
room_array = ["EV009.241", "EV009.245"]
room_data = list(database.keys())
result = {}
for i in range(len(room_data)):
    if room_data[i] in room_array:
        result[room_data[i]] = database[room_data[i]]

print(result)

# URL = 'https://aits.encs.concordia.ca/assets/encs/html/Software%20for%20Windows%20in%20the%20Public%20Labs.html'
# myScraper = Scraper(URL)
# tags = myScraper.get_list_from_tag("tr", "td")

# print(tags)


# myScraper = Scraper()
# tags = myScraper.get_list_from_tag("tr", "td")
# software_array = ["Acrobat_Pro_DC", "Android_Studio_V3_5_2"]
# list_of_all_room = []
# for i in tags:
#     if i[0] in software_array:
#         # separate room string into list of room 
#         list_of_room = [i.split(",") for i in i[1::]]
#         # turn nested lists into 1 flat list
#         list_of_room = [item.strip() for sublist in list_of_room for item in sublist]
#         # add rooms to result list
#         list_of_all_room.append(list_of_room)
# # turn nested lists into 1 flat list
# list_of_all_room = [item for sublist in list_of_all_room for item in sublist]
# # # remove duplicates
# list_of_all_room = list(set(list_of_all_room))

# print(list_of_all_room)
