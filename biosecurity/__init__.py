from flask import Flask

app = Flask(__name__)
app.secret_key = 'Summer*secrect@2024'
app.config['UPLOAD_FOLDER'] = 'biosecurity/static/img/'

from biosecurity import login
from biosecurity import admin
from biosecurity import staff
from biosecurity import mariner
from biosecurity import shared