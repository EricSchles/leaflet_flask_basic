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

setLatLng - This method captures the latitude/longitude that was clicked and saves it to the popup object, binding the marker to the location you clicked.
setContent -  This method displays the latitude/longitude
openOn - opens the popup object and displays the associated content

Finnally we have - map.on('click',onMapClick):

This method turns on the click action for the map, and sets it to the function we created.  Notice that we have one global popup object that gets changed as we click on different places in the map.



