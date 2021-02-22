from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin

from scraper.scraper import Scraper
from scraper.scraper_encs import *

from dotenv import load_dotenv
from pathlib import Path


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/hello')
def hello():
    return "Hello CoCo!"

@app.route('/')
def main():
    return render_template("index.html")


@cross_origin()
@app.route('/fetchSoftwareName')
def fetch_software_name():
    myScraper = Scraper()
    tags = myScraper.get_list_from_tag("tr", "td")
    software = []
    for i in tags:
        software.append(i[0])
    return {"result": software}


@cross_origin()
@app.route('/room_by_software', methods=["POST"])
def fetch_room():
    myScraper = Scraper()
    tags = myScraper.get_list_from_tag("tr", "td")
    software_array = request.json['software_array']
    list_of_all_room = []
    for i in tags:
        if i[0] in software_array:
            # separate room string into list of room 
            list_of_room = [i.split(",") for i in i[1::]]
            # turn nested lists into 1 flat list
            list_of_room = [item.strip() for sublist in list_of_room for item in sublist]
            # add rooms to result list
            list_of_all_room.append(list_of_room)
    # turn nested lists into 1 flat list
    list_of_all_room = [item for sublist in list_of_all_room for item in sublist]

    # If there are more than 1 software required
    if len(software_array) > 1: 
        # find rooms that appear more than 1
        list_of_all_room = list(set([i for i in list_of_all_room if list_of_all_room.count(i) > 1]))
    
    # reformat rooms number
    list_of_all_room = reformat_room_number(list_of_all_room)
    return {"result": list_of_all_room}

# helper function to reformat list of room numbers from "H0823-00" to "H823"
def reformat_room_number(room_numbers:list) -> list:
    formated_room_numbers = []
    for i in room_numbers:
        if i[0] == "H":
            room = "H" + i[2:5] # all labs in Hall Building start with "H" and have 3 digits number
            formated_room_numbers.append(room)
        else: # is labs in "EV" buidling replace "-" with "." e.g. from "EV009-241" to "EV009.241"
            room = i.replace("-", ".")
            formated_room_numbers.append(room)
    return formated_room_numbers


@cross_origin()
@app.route('/get_lab_host_by_software', methods=["POST"])
def fetch_host():
    database = scrape(os.environ.get("ENCS_LOGIN_NAME"), os.environ.get("ENCS_PASSWORD"))
    room_array = request.json['room_array']
    room_array = reformat_room_number(room_array)
    # room_array = ["EV009.241", "EV009.245"]
    room_data = list(database.keys())
    result = {}
    for i in range(len(room_data)):
        if room_data[i] in room_array:
            result[room_data[i]] = database[room_data[i]]
    return result

if __name__ == "__main__":
    app.run(debug=True)