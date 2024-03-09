from flask import Flask
from flask_hashing import Hashing

app = Flask(__name__)
app.secret_key = 'Summer*secrect@2024'
app.config['UPLOAD_FOLDER'] = 'app/static/img/'

from biosecurity import login
from biosecurity import admin
from biosecurity import staff
from biosecurity import mariner
from biosecurity import shared