from flask import Flask
from flask import render_template
import os
import requests
import json

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('welcome.html')


@app.route('/health')
def health_check():
    return "Success"


@app.route('/page')
def page():
    backend_url = get_config("backend_url")
    resp = requests.get("http://{}".format(backend_url))
    print(resp, flush=True)
    txt = resp.text
    print(txt, flush=True)
    response_json = json.loads(txt)
    print(response_json, flush=True)
    return render_template('page.html', response_json=response_json)


def get_config(key):
    if os.environ.get(key):
        return os.environ.get(key)
    else:
        return None
