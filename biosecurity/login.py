from flask import render_template, request, redirect, url_for, session, flash
from datetime import datetime, date

from biosecurity import app
from flask_hashing import Hashing
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
                user_id = ACCOUNT[0]
                user_name= ACCOUNT[1]
                password =  ACCOUNT[2]
                user_role = ACCOUNT[3]

                if user_role == "admin":
                    if hashing.check_value(password, input_password, salt='rainbow'):
                        session['loggedin'] = True
                        session['user_id'] = user_id
                        session['username'] = user_name
                        session['user_role'] = user_role                  
                        return redirect(url_for('adminHome'))
                    else:
                        flash("Incorrect password. Please try again.", "error")
                        return render_template("login.html")
                    
                if user_role == "staff":
                    sql1="SELECT active_user FROM staff WHERE user_id = %s;"
                    cursor.execute(sql1, (user_id,))
                    active_staff = cursor.fetchone()[0]
                    if active_staff == 0:
                        flash("Your account has been inactivated. Please contact the admin.", "error")
                        return render_template("login.html")
                    else:
                        if hashing.check_value(password, input_password, salt='rainbow'):
                            # If account exists in the database, create session data
                            session['loggedin'] = True
                            session['user_id'] = user_id
                            session['username'] = user_name
                            session['user_role'] = user_role
                            return redirect(url_for('staffHome'))
                        else: 
                            flash("Incorrect password. Please try again.", "error")
                            return render_template("login.html")
                                            
                if user_role == "mariner":
                    sql2="SELECT active_user FROM mariner WHERE user_id = %s;"
                    cursor.execute(sql2, (user_id,))
                    active_mariner = cursor.fetchone()[0]
                    if active_mariner == 0:
                        flash("Your account has been inactivated. Please contact the admin.", "error")
                        return render_template("login.html")
                    else:
                        if hashing.check_value(password, input_password, salt='rainbow'):
                            # If account exists in the database, create session data
                            session['loggedin'] = True
                            session['user_id'] = user_id
                            session['username'] = user_name
                            session['user_role'] = user_role
                            return redirect(url_for('marinerHome'))
                        else: 
                            flash("Incorrect password. Please try again.", "error")
                            return render_template("login.html")                
            else:
                # Account doesn't exist or username incorrect
                flash("User not found. Please try again.", "error")
                return render_template("login.html")
        else:        # User does not attempt to log in, show the login page
            return render_template("login.html")
        
    

@app.route("/register", methods=["GET", "POST"])
def register():
    cursor = getCursor()
    today = date.today()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password1")
        hashed_password = hashing.hash_value(password, salt='rainbow')

        first_name = request.form.get("first_name").capitalize()
        last_name = request.form.get("last_name").capitalize()
        phone = request.form.get("phone")
        address = request.form.get("address")
        email = request.form.get("email")
        date_joined = request.form.get("date_joined")

        # Check if the entered username already exists in the database
        sql1 = "SELECT * FROM user WHERE username = %s;"
        cursor.execute(sql1, (username,))
        ACCOUNT = cursor.fetchone()
       
        if ACCOUNT is not None:
            flash("Username already exists. Please choose a different username.", "error")
            return redirect(url_for('register'))
        else:
            # Username is available, continue to register the account
            sql2 = """
                START TRANSACTION;
                INSERT INTO user (username, password) VALUES (%s, %s);
                INSERT INTO mariner (first_name, last_name, email, phone, address, date_joined, user_id) 
                VALUES (%s, %s, %s, %s, %s, %s, LAST_INSERT_ID());
                COMMIT;
                """
            cursor.execute(sql2, (username, hashed_password, first_name, last_name, email, phone, address, date_joined))
            flash("Account created successfully. Please login.", "success")
            return redirect(url_for('login'))
    else:
        return render_template("register.html", today=today)   
 

@app.route("/logout")
def logout():
    # Remove session data to log the user out
   session.pop('loggedin', None)
   session.pop('user_id', None)
   session.pop('username', None)
   session.pop('user_role', None)
   # Redirect to login page
   return redirect(url_for('login'))
