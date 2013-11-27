#!/usr/bin/env python
import sys

from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about/")
def about():
    return render_template('about.html')

@app.route("/why_crb/")
def why_crb():
    return render_template('why_crb.html')

@app.route("/members/")
def members():
    return render_template('members.html')

@app.route("/certified-products/")
def certified_products():
    return render_template('certified_products.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        app.config['FREEZER_RELATIVE_URLS'] = True
        freezer.freeze()
    else:
        app.debug = True
        app.run(port=8000)
