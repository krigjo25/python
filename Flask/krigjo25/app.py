#   Importing responsories
from flask import Flask, flash, redirect, render_template, requests, session
from flask_session import Session
from markupsafe import Markup

#   Custom libs
from lib.config.config import DevelopmentConfig
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config.from_object(DevelopmentConfig)
Session(app)

#   Database Connection
db = SQL()

@app.after_request
def after_request(response):
    """Ensure the responses aren't cached"""
    response.headers['Cache-Control'] = "no-cache, no-store, must-revalidate"
    response.headers['Expires'] = 0
    response.headers['Paragma'] = 'no-cache'
    return response

@app.route('/')
def index():

    """ Show Portefolio from database"""

    protefolio = 0

    return render_template('index.html', protefolio = portefolio)

