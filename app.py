from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import re
from datetime import datetime, date
import mysql.connector
from mysql.connector import FieldType
import connect

app = Flask(__name__)

cursor = None
connection = None

def getCursor():
    global cursor
    global connection
    connection = mysql.connector.connect(user=connect.dbuser, \
    password=connect.dbpass, host=connect.dbhost, \
    database=connect.dbname, autocommit=True)
    cursor = connection.cursor()
    return cursor


@app.route("/")
def home():
    return render_template("home.html")