#Working with Leaflet

Leaflet is a wonderful library.  It allows you to visualize a whole bunch of information, geographically!  One of the things I've gotten into recently is making use of GIS maps to show my boss and other folks how their data looks.  Making use of leaflet allows us to make this super pretty.

With leaflet we can do things like, create polygons, add visual representations of data, add paths, create heat maps, and add various layers of control and interactivity.  

All and all, leaflet lets us visualy interogate a ton of data and do so in an easy and fun way!  With something very visually pleasing.  

So enough talk, let's look at how to make use of leaflet, with this basic example, [lifted directly from their docs](http://leafletjs.com/examples/quick-start.html):

http://leafletjs.com/examples/quick-start-example.html

Let's start by looking at the head of the html page:

```
<head>
	<title>Leaflet Quick Start Guide Example</title>
	<meta charset="utf-8" />

	<meta name="viewport" content="width=device-width, initial-scale=1.0">

	<link rel="stylesheet" href="http://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.3/leaflet.css" />
</head>
```

Here we include the necessary CSS via a CDN (content delivery network), note that the official documentation says to use 0.7.4 but when I tried it 0.7.3 is the one that worked.  I'm not sure how long this will be true for, but for now, please use 0.7.3.  

Now let's look at the body of the html, up to the script tag:

```
<body>
<div id="map" style="width: 600px; height: 400px"></div>
 <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.3/leaflet.js"></script>
 <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.3/leaflet-src.js"></script>
```

Here we see that we add our map in a div tag, with id "map".  Notice also that we set a width and height - this is super important otherwise our map won't appear.  Notice also that we load the leaflet javascript AFTER the map.  This may not matter on your system, but it did matter on mine.  

Now let's look at the map script, which comes after loading leaflet.js:

```
<script>
	var map = L.map('map').setView([51.505, -0.09], 13);

	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6IjZjNmRjNzk3ZmE2MTcwOTEwMGY0MzU3YjUzOWFmNWZhIn0.Y8bhBaUMqFiPrDRW9hieoQ', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
			'<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery © <a href="http://mapbox.com">Mapbox</a>',
		id: 'mapbox.streets'
	}).addTo(map);


	L.marker([51.5, -0.09]).addTo(map)
		.bindPopup("<b>Hello world!</b><br />I am a popup.").openPopup();

	L.circle([51.508, -0.11], 500, {
		color: 'red',
		fillColor: '#f03',
		fillOpacity: 0.5
	}).addTo(map).bindPopup("I am a circle.");

	L.polygon([
		[51.509, -0.08],
		[51.503, -0.06],
		[51.51, -0.047]
	]).addTo(map).bindPopup("I am a polygon.");


	var popup = L.popup();

	function onMapClick(e) {
		popup
			.setLatLng(e.latlng)
			.setContent("You clicked the map at " + e.latlng.toString())
			.openOn(map);
	}

	map.on('click', onMapClick);

	</script>
```

There is a lot to unpack here, so we'll go through it line by line:


`var map = L.map('map').setView([51.505, -0.09], 13);`

On this line we instantiate our map object and link it to the map id in our div tag.  To understand this constructor in more detail, check out [the reference](http://leafletjs.com/reference.html#map-constructor).  

Notice that we chain this object with a setView method - which sets the geographic coordinates that our map will start at and the zoom level.  [Here is the referenece for setView](http://leafletjs.com/reference.html#map-options)

Next we pull in a tiling.  This is how the map will look.  Leaflet's documentation recommends Mapbox's tiling system.  So we'll make use of it.  Head over to [mapbox](https://www.mapbox.com/) to get api access.


Here's how you add tiling:

```
L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6IjZjNmRjNzk3ZmE2MTcwOTEwMGY0MzU3YjUzOWFmNWZhIn0.Y8bhBaUMqFiPrDRW9hieoQ', {
	maxZoom: 18,
	attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
		'<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
		'Imagery © <a href="http://mapbox.com">Mapbox</a>',
	id: 'mapbox.streets'
}).addTo(map);
```

Basically we are mapping a request to the mapbox api with a maximum zoom, attribution, and id preset.  Notice that we also pass in an access token in this case, the string: pk.eyJ1IjoibWFwYm94IiwiYSI6IjZjNmRjNzk3ZmE2MTcwOTEwMGY0MzU3YjUzOWFmNWZhIn0.Y8bhBaUMqFiPrDRW9hieoQ which clearly is randomly generated.  

Notice that we are creating a tileLayer object and then adding it to our map layer.  Essentially, we can think of these data structures as components of a map object is sort of like the base visual representation but it is ultimately an abstraction.  The tile layer is what gives it a visual form.  In this case we pull in the look of the tiling from the tile layer.  And then we can super impose other structures ontop of the tile layer.  

We see this pattern in the remaining objects we add to our map:

```
L.marker([51.5, -0.09]).addTo(map)
	.bindPopup("<b>Hello world!</b><br />I am a popup.").openPopup();

L.circle([51.508, -0.11], 500, {
	color: 'red',
	fillColor: '#f03',
	fillOpacity: 0.5
}).addTo(map).bindPopup("I am a circle.");

L.polygon([
	[51.509, -0.08],
	[51.503, -0.06],
	[51.51, -0.047]
]).addTo(map).bindPopup("I am a polygon.");
```

The marker, circle and polygon are all examples of objects that take up a discrete piece of the map:

* A marker takes up a single point in this case - (51.5, -0.09).  

* The circle has both a center and radius, in this case - [(51.508,-0.11), 500].

* The polygon has just a set of coordinates, connected by points: [51.509,-0.08], [51.503,-0.06], [51.51, -0.047]

Notice that we simply chain the various shapes to our map data structure, and then add bindPopups to each, identifying what the object's data is.  Notice of course that we could have had anything in the data since we can embed html.  

Now that we understand the objects that must be loaded from the server, let's understand the elements of the code that are dynamic from the front end:

```
var popup = L.popup();

function onMapClick(e) {
	popup
		.setLatLng(e.latlng)
		.setContent("You clicked the map at " + e.latlng.toString())
		.openOn(map);
}

map.on('click', onMapClick);
```

Here we create a popup object.  Notice that we make use of this popup object by wrapping it in a function that calls three of it's methods:

`setLatLng` - This method captures the latitude/longitude that was clicked and saves it to the popup object, binding the marker to the location you clicked.
`setContent` -  This method displays the latitude/longitude
`openOn` - opens the popup object and displays the associated content

Finnally we have - `map.on('click',onMapClick)`:

This method turns on the click action for the map, and sets it to the function we created.  Notice that we have one global popup object that gets changed as we click on different places in the map.

So now we understand a lot of what Leaflet.js can do, which is great.  Of course, all of this was static, as far as the data goes.  By making use of server, which can request different data points you can:

* filter by different data points, 
* bring in different data sets, 
* extrapolate data points,
* regroup the data elements dynamically, according to some clustering algorithm

Clearly this adds a whole layer of flexibility and dynamics that would otherwise be lost.  So how do we do that?

Let's start with the most basic server and templated html possible:

server.py:

```
import json
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    states = [{
        "type":"Feature",
        "properties": {"party": "Republican"},
        "geometry": {
            "type": "Polygon",
            "coordinates": [[
                [-104.05, 48.99],
                [-97.22,  48.98],
                [-96.58,  45.94],
                [-104.03, 45.94],
                [-104.05, 48.99]
            ]]
        }
    }, {
        "type": "Feature",
        "properties": {"party": "Democrat"},
        "geometry": {
            "type": "Polygon",
            "coordinates": [[
                [-109.05, 41.00],
                [-102.06, 40.99],
                [-102.03, 36.99],
                [-109.04, 36.99],
            [-109.05, 41.00]
            ]]
        }
    }]

    return render_template("index.html",states=json.dumps(states))
```

Here we have a simple flask app, the only difference is the static geojson - stored as a python dictionary.  Notice the necessary pieces - type, properties, geometry.  These are all the necessary keys. The geometry key is where the lat/long actually lives.  Notice that we make use of json.dumps to pass our states to the front end.  After that our application is complete.  As a next example, let's look at a real-time map - that is continually populated from an api.

##Our API

Since we already know what geojson should look like, building an api shoudl be easy:

```
from flask import Flask, render_template, redirect, url_for
import random
import json
app = Flask(__name__)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response

@app.route("/send_areas",methods=["GET","POST"])
def send_areas():
    areas = [{
        "type":"Feature",
        "properties": {"glob": "1st"},
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [[random.randint(100,106) + random.random(), random.randint(44,49) + random.random()] for i in xrange(4)]
            ]
        }
    }, {
        "type": "Feature",
        "properties": {"glob": "2nd"},
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [[random.randint(100,106) + random.random(), random.randint(44,49) + random.random()] for i in xrange(4)]
            ]
        }
    }]
    return json.dumps(areas)

app.run(debug=True,port=5001,threaded=True)
```

Notice that, except for the randomly generated data, everything here is exactly the same as our last example.  However there is something new here:

```
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response
```

Since we'll be running both a server and api, we'll need to allow for cross origin from both the server and client side.  We'll handle the front end piece in a second.  But here is the server side - essentially this is just appending authorization to the header.  Notice that we allow GET,PUT,POST, and DELETE methods.  We are also giving full access via Access-Control-Allow-Origin, *.  The * means all domains are allowed to access our api.  Of course, we could restrict this to just a single domain or a list of domains.  If this were a closed API or an api that required some kind of authentication that would be best.  However, this is randomly generated data so we are not in any sort of danger by making it completely open.  

Now onto the front end real-time piece:

For this we'll make use of an extention of leaflet.js which can be found here - [realtime-leaflet.js](https://github.com/perliedman/leaflet-realtime)

Here is our server:

```
from flask import Flask

app = Flask(__name__)

@app.route("/realtime",methods=["GET","POST"])
def realtime():
    return render_template("realtime.html")

app.run()
```

Notice it is as simple as possible.  Next let's look at realtime.html:

```
<html>
<head>
    <title>Leaflet Realtime</title>
    <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.7.3/leaflet.css" />
    
</head>
<body>
    <div id="map" style="width: 600px; height: 400px"></div>

    <!-- source: https://github.com/perliedman/leaflet-realtime -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.3/leaflet.js"></script>
    <script src="http://cdn.leafletjs.com/leaflet-0.7.3/leaflet-src.js"></script>
    <script src="{{ url_for('static', filename='js/leaflet-realtime.js') }}"></script>
    <script src=" {{ url_for('static', filename='js/index.js') }}"></script>
</body>
</html>
```

Notice that it too is very simple.  Most of this is just including the necessary javascript libraries.  The only file we really care about is index.js, which we'll look at next.  Notice that we also include a file called leaflet-realtime.js which we got from the github repo for realtime-leaflet.js  

index.js:

```
var map = L.map('map'),
    realtime = L.realtime({
        url: 'http://localhost:5001/send_areas', /*'https://wanderdrone.appspot.com/' - works for sure */
        crossOrigin: true,
        type: 'json'
    }, {
        interval: 3 * 1000
    }).addTo(map);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6IjZjNmRjNzk3ZmE2MTcwOTEwMGY0MzU3YjUzOWFmNWZhIn0.Y8bhBaUMqFiPrDRW9hieoQ', {
	maxZoom: 18,
	attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
		'<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
		'Imagery © <a href="http://mapbox.com">Mapbox</a>',
	id: 'mapbox.streets'
	}).addTo(map);

realtime.on('update', function() {
    map.fitBounds(realtime.getBounds(), {maxZoom: 3});
});
```

As you can see there isn't a lot new here either.  The major difference is the map object which has crossOrigin set to true (allowing us to access our API like we did on the api side) setting our interval (how often we make calls out to our api) and adding our realtime map to the map object.  Note that the tileLayer is exactly the same as before.  Finally we turn realtime 'on' by calling realtime's on method.  We set the method to update (meaning it will make calls to the api) and we pass in a function which sets some configuration.  In this case the anonymous function simply sets the bounds, which are preset and then sets the maxZoom (how zoomed into the map we are).  
to see our code in action you can check out [this repo] and then run the following code:

first we start up the api:

`python geo_json_api.py`

Then start the server:

python server.py

Then open a web browser and head to - [http://localhost:5000/realtime](http://localhost:5000/realtime)



How might we use this?  An interesting use might be setting up our api to pull from a series of open data sources, like New York City's open real time apis and marrying that with say turnstyle data.  Watching how city complaints marry with city subway usage might be an interesting experiment.  Of course, the content our api serves over time would need to grow, each request serving more and more content or we'd only see one data point at a time.  