#   Importing responsories
import os
from dotenv import load_dotenv
from markupsafe import Markup
from flask_session import Session
from flask import Flask, flash, redirect, render_template, request, session


#   Custom libs
from lib.config.config import DevelopmentConfig
from lib.db.databases  import SQL


load_dotenv()
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config.from_object(DevelopmentConfig)
Session(app)

#   Database Connection
db = SQL(os.getenv('db'))

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

    image = db.selectRecord('photos')
    education = db.selectRecord('edx')
    
    pe= db.selectRecord('proend')
    pb = db.selectRecord('bapro')

    return render_template('index.html')

