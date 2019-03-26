from flask import Flask, flash, redirect, render_template, request, session, abort

import sys
import os
import json
import requests
import urllib

# settings.py
from dotenv import load_dotenv
load_dotenv()
USERNAME = os.getenv("USERNAME")
APIKEY = os.getenv("APIKEY")


def get_models(username, api_key):
    """ Send a GET request to Wayfair 3D model API to get all 3D models

        Args:
        username: API username
        api_key: API key

        Returns:
        A JSON response for 3D model information
    """

    url = "https://wayfair.com/3dapi/models"

    # use session to send auth and header along with every request
    session = requests.Session()
    session.auth = (username, api_key)
    session.headers = {'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36'}
    session.get(url)
    response = session.get(url)
    return response.json()

app = Flask(__name__)

@app.route("/")
def index():
    # Send a GET request to Wayfair 3D model API to get the JSON for all 3D models
    response = get_models(USERNAME, APIKEY)
    print(type(response))
    #response_objects = json.load(responses)
    print ('Number of returned 3D models: ',len(response))

    if len(response) != 188:
        print ('''
            If you are only getting 5 models back, this is probably because
            you are entering wrong username/api_key. Make sure you signed
            up for an API key at https://wayfair.com/3dapi
            ''')

    print ('\n')
    print ('Now downloading 3D models to Wayfair 3D Models/ folder')
    #print(response_objects)
    return render_template('index.html', response=response)

@app.route("/product/<sku>")
def product(sku):
    return render_template('product.html',sku=sku)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)