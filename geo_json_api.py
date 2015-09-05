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
