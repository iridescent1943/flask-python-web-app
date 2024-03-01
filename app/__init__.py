from flask import Flask

app = Flask(__name__)
app.secret_key = 'Summer*secrect@2024'

from app import login
from app import admin
from app import staff
from app import mariner
from app import shared