import json
from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import requests
import datetime
from edgarapi import get_cik, get_edgar, DEFAULT_EDGAR_METRIC
from tvapi import get_tv

today = datetime.date.today()
YEAR = today.year

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify("Hello, API!")

@app.route('/edgar/')
def edgar_api():
    name = request.args.get("name")
    CIK = request.args.get("CIK")
    start = request.args.get("start")
    end = request.args.get("end")
    form = request.args.get("form")
    
    if not (name or CIK):
        return jsonify("Name of the company or the CIK code needs to be provided."), 400 
    if name:
        CIK =  get_cik(name)[0]["code"]
    metrics = request.args.getlist("metric") 
    if not metrics:
        metrics = DEFAULT_EDGAR_METRIC
    if not end:
        end = YEAR
    if not form:
        form = "10-Q"

    data = get_edgar(CIK, metrics, start, end, form)
    status_code = data["status_code"]
    return jsonify(data["content"]), status_code

@app.route('/tv/')
def tv_api():
    name = request.args.get("name")
    statement = request.args.get("statement")
    
    if not (name and statement):
        return jsonify("Name and statement needs to be provided."), 400
    
    data = get_tv(name, statement)

    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)
