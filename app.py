"""
Flask app for the web application
"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    #read the contentens of out.txt
    with open('out.txt', 'r') as file:
        data = file.read()
    return render_template('index.html', data=data)

