from flask import Flask, render_template
from datetime import datetime
from urllib.parse import urlencode
import csv
import requests

GMAPS_URL = 'https://maps.googleapis.com/maps/api/staticmap?'
USGS_FEED_URL = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.csv'


## helper functions
# should probably go into their own file but too lazy to do that

def get_quake_data():
    resp = requests.get(USGS_FEED_URL)
    data = list(csv.DictReader(resp.text.splitlines()))
    # we need to format time separately
    return data


def simple_static_gmap_url(location):
    # This just returns a URL string, it doesn't get the URL via requests
    mydict = {'size': '300x200', 'maptype': 'hybrid', 'markers': location}
    url = GMAPS_URL + urlencode(mydict, doseq=True)
    return url


# Normal flask app stuff

app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    the_quakes = get_quake_data();

    # iterate through each quake, give them a "latlng" attribute
    # and then a separate Google Map URL
    for q in the_quakes:
        q['latlng'] = q['latitude'] + ',' + q['longitude']
        q['gmap_url'] = simple_static_gmap_url(q['latlng'])

    html = render_template('homepage.html',
                            time=the_time, quakes=the_quakes)
    return html


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

