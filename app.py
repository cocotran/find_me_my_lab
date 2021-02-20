from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin

from scraper.scraper import Scraper
from scraper.scraper_encs import *

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
    URL = 'https://aits.encs.concordia.ca/assets/encs/html/Software%20for%20Windows%20in%20the%20Public%20Labs.html'
    myScraper = Scraper(URL)
    tags = myScraper.get_list_from_tag("tr", "td")
    software = []
    for i in tags:
        software.append(i[0])
    return {"result": software}


@cross_origin()
@app.route('/get_lab_host_by_software', methods=["POST"])
def scrape_encs():
    database = scrape()
    room_array = request.json['room_array']
    room_data = list(database.keys())
    result = {}
    for i in range(len(room_data)):
        if room_data[i] in room_array:
            result[room_data[i]] = database[room_data[i]]
    return result

if __name__ == "__main__":
    app.run(debug=True)