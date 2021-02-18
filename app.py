from scraper.scraper import Scraper
from flask import Flask, render_template
from flask_cors import CORS, cross_origin

from scraper.scraper import *

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


if __name__ == "__main__":
    app.run(debug=True)