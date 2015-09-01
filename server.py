#This basic server will send data to the leaflet frontend
from random import randint
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

@app.route("/basic",methods=["GET","POST"])
def basic():
    return render_template("basic.html")

app.run(debug=True)
