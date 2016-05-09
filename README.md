# Less Simple Flask Earthquakes app


This is a more complicated version of the Basic Heroku Flask App lesson: [https://github.com/datademofun/heroku-basic-flask](https://github.com/datademofun/heroku-basic-flask).

It contains a skeleton of a Flask app that talks to the Google Maps API and USGS earthquake data.

A more polished project can be found at: [https://github.com/datademofun/heroku-flask-quakes-lesssimple](https://github.com/datademofun/heroku-flask-quakes-lesssimple)


# Tasks

Try to add the features found in the [lesssimple version of this app](https://github.com/datademofun/heroku-flask-quakes-lesssimple) and deploy it to Heroku.

The features include:

1. Each place name of an earthquake should link to the earthquake's official USGS eventpage URL, i.e. [http://earthquake.usgs.gov/earthquakes/eventpage/us10005c88](http://earthquake.usgs.gov/earthquakes/eventpage/us10005c88)
2. Each row should show the correct Google static map, not an image of Stanford.
3. There should be a Google static map that shows every earthquake.

# About the data

Earthquake data comes from the USGS: http://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php


## How to create a URL for a Google static map

Example Google Static Map URL: 

[https://maps.googleapis.com/maps/api/staticmap?size=600x300&markers=Stanford,CA](https://maps.googleapis.com/maps/api/staticmap?size=600x300&markers=Stanford,CA)

What it looks like:

![static map](https://maps.googleapis.com/maps/api/staticmap?size=600x300&markers=Stanford,CA)


Google documentation for the static maps API: https://developers.google.com/maps/documentation/static-maps/intro#URL_Parameters


Some examples of how to use the [__urllib.parse.urlencode__ method to create complicated query strings](http://2016.compciv.org/guides/python/how-tos/creating-proper-url-query-strings/).

Try this out:

~~~py
from urllib.parse import urlencode
GMAPS_URL = 'https://maps.googleapis.com/maps/api/staticmap?'
locations = ['Stanford, CA', 'Berkeley, CA', 'Napa, CA']
myparams = {'size': '800x400', 'maptype': 'satellite', 'markers': locations}

url = GMAPS_URL + urlencode(myparams, doseq=True)
# https://maps.googleapis.com/maps/api/staticmap?size=800x400&maptype=satellite&markers=Stanford%2C+CA&markers=Berkeley%2C+CA&markers=Napa%2C+CA
~~~


Which renders this map:

![california map](https://maps.googleapis.com/maps/api/staticmap?size=800x400&maptype=satellite&markers=Stanford%2C+CA&markers=Berkeley%2C+CA&markers=Napa%2C+CA)
