from flask import Flask
from flask_hashing import Hashing

app = Flask(__name__)
app.secret_key = 'Summer*secrect@2024'
app.config['UPLOAD_FOLDER'] = 'app/static/img/'
hashing = Hashing(app)

from app import login
from app import admin
from app import staff
from app import mariner
from app import shared