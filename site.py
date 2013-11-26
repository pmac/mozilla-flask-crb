#!/usr/bin/env python
from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == "__main__":
    app.debug = True
    app.run(port=8000)
