from flask import render_template, request, redirect, url_for, session, flash
from flask_hashing import Hashing
from app import app
hashing = Hashing(app)

import mysql.connector
from mysql.connector import FieldType
import connect

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
def visit():
    return redirect (url_for('login'))

@app.route("/login", methods=["GET", "POST"])
def login():  
    cursor = getCursor() 
    if 'loggedin' in session:
        if session['user_role'] == "admin":
            return redirect(url_for('adminHome'))
        if session['user_role'] == "staff":
            return redirect(url_for('staffHome'))
        if session['user_role'] == "mariner":
            return redirect(url_for('marinerHome'))
    else:
        if request.method == "POST":
            username = request.form.get("username")
            input_password = request.form.get("password")
            # Check if account exists in the database
            sql = "SELECT * FROM user WHERE username = %s;"
            cursor.execute(sql, (username,))
            ACCOUNT = cursor.fetchone()
            if ACCOUNT is not None:
                password =  ACCOUNT[2]
                # Check if the password is correct
                if hashing.check_value(password, input_password, salt='rainbow'):
                    # If account exists in the database, create session data
                    session['loggedin'] = True
                    session['user_id'] = ACCOUNT[0]
                    session['username'] = ACCOUNT[1]
                    session['user_role'] = ACCOUNT[3]
                    # Redirect to different home pages based on the role of the user
                    if session['user_role'] == "admin":
                        return redirect(url_for('adminHome'))
                    if session['user_role'] == "staff":
                        return redirect(url_for('staffHome'))
                    if session['user_role'] == "mariner":
                        return redirect(url_for('marinerHome'))                
                else:
                    # Password incorrect             
                    flash("Incorrect password. Please try again.", "error")
                    return render_template("login.html")
            else:
                # Account doesn't exist or username incorrect
                flash("Incorrect username. Please try again.", "error")
                return render_template("login.html")
        else:        # User does not attempt to log in, show the login page
            return render_template("login.html")
        
    

@app.route("/register", methods=["GET", "POST"])
def register():
    cursor = getCursor()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        hashed_password = hashing.hash_value(password, salt='rainbow')
        email = request.form.get("email")
        # Check if the entered username already exists in the database
        sql1 = "SELECT * FROM user WHERE username = %s;"
        cursor.execute(sql1, (username,))
        ACCOUNT = cursor.fetchone()
        if ACCOUNT is not None:
            print("Username already exists. Please choose a different username.")
        else:
            # Username is available, continue to register the account
            sql2 = "INSERT INTO user (username, password, email) VALUES (%s, %s, %s);"
            cursor.execute(sql2, (username, hashed_password, email))
            print("Account created successfully. Please login.")
            return redirect(url_for('login'))
    else:
        return render_template("register.html")   
 

@app.route("/logout")
def logout():
    # Remove session data to log the user out
   session.pop('loggedin', None)
   session.pop('user_id', None)
   session.pop('username', None)
   session.pop('user_role', None)
   # Redirect to login page
   return redirect(url_for('login'))
