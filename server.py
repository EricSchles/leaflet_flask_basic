#This basic server will send data to the leaflet frontend
from random import randint
import json
from flask import Flask, render_template, g, flash, redirect, request, url_for 
from flaskext import uploads
import pandas as pd 
import os
from werkzeug import secure_filename
from glob import glob

UPLOAD_FOLDER = os.getcwd() + "/static/uploads"
ALLOWED_EXTENSIONS = set(['csv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/<filename>",methods=["GET","POST"])
@app.route("/",methods=["GET","POST"])
def index(filename=None):
    datasets = [File.split("/")[-1] for File in glob("static/uploads/*")]
    if filename:
        full_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.exists(full_path):
            return render_template("index.html",states=json.dumps(transform_csv(full_path)),datasets=datasets)
        return "fail"
    else:
        return render_template("index.html",states=json.dumps([{}]),datasets=datasets)

@app.route("/basic",methods=["GET","POST"])
def basic():
    return render_template("basic.html")

@app.route("/realtime",methods=["GET","POST"])
def realtime():
    return render_template("realtime.html")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/listing_of_datasets",methods=["GET","POST"])
def listing_of_datasets():
    if request.method == "POST":
        dataset = request.form.get("datasets")
    return redirect(url_for("index")+dataset)

def transform_csv(filename):
    df = pd.DataFrame.from_csv(filename,index_col=False)
    json_data = df.to_json()
    data = []
    for row in df.iterrows():
        datum = {}
        tmp_dict = row[1].to_dict()
        print tmp_dict
        datum["geometry"] = {
            "type" : "Point",
            "coordinates":[tmp_dict["lat"],tmp_dict["long"]]
            }
        datum["type"] = "Feature"
        datum["properties"] = tmp_dict
        data.append(datum)
    return data

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for("index"))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


app.run(debug=True)
