from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import flash

from app import app
from flask_hashing import Hashing
hashing = Hashing(app)

from app.shared import getCursor
from app.shared import home
from app.shared import adminOrStaffProfile
from app.shared import editAdminOrStaffProfile
from app.shared import changePassword
from app.shared import marinerList
from app.shared import guideList
from app.shared import addGuide

@app.route("/admin/home")
def adminHome():
    if "loggedin" in session and session["user_role"] == "admin":
        return home()
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login'))


@app.route("/admin/profile", methods=["GET"])
def adminProfile(): 
    if "loggedin" in session and session["user_role"] == "admin":
        return adminOrStaffProfile()
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login'))


@app.route("/admin/profile/edit", methods=["GET", "POST"])
def editAdminProfile():
    if "loggedin" in session and session["user_role"] == "admin":
        return editAdminOrStaffProfile()
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login'))
    

@app.route("/admin/changepassword", methods=["GET", "POST"])
def adminChangePassword():
    if "loggedin" in session and session["user_role"] == "admin":
        return changePassword()
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login'))
    

@app.route("/admin/stafflist")
def staffList():    
    if 'loggedin' in session and session["user_role"] == "admin":
        user_role = session.get('user_role')
        cursor = getCursor()
        sql = "SELECT * FROM staff"
        cursor.execute(sql)
        ALL_STAFF = cursor.fetchall()
        return render_template('staff_list.html', user_role= user_role, all_staff=ALL_STAFF)
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login'))
    
    
@app.route("/admin/staff/add", methods=["GET", "POST"])
def addStaff():
    if 'loggedin' in session and session["user_role"] == "admin":
        user_role = session.get('user_role')
        cursor = getCursor()
        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")
            hashed_password = hashing.hash_value(password, salt='rainbow')
            email = request.form.get("email")
            first_name = request.form.get("first_name")
            last_name = request.form.get("last_name")
            work_phone = request.form.get("work_phone")
            department = request.form.get("department")
            position = request.form.get("position")
            hire_date = request.form.get("hire_date")
            # Check if the entered username already exists in the database
            sql1 = "SELECT * FROM user WHERE username = %s;"
            cursor.execute(sql1, (username,))
            ACCOUNT = cursor.fetchone()
            if ACCOUNT is not None:
                return "Username already exists. Please choose a different username."
            else:
                # Username is available, continue to register the account
                sql2 = "INSERT INTO user (username, password, email, user_role) VALUES (%s, %s, %s, 'staff');"
                cursor.execute(sql2, (username, hashed_password, email))
                user_id = cursor.lastrowid
                sql3 = "INSERT INTO staff (user_id, first_name, last_name, work_phone, department, position, hire_date) VALUES (%s, %s, %s, %s, %s, %s, %s);"
                cursor.execute(sql3, (user_id, first_name, last_name, work_phone, department, position, hire_date))
                return redirect(url_for('staffList'))
        else:
            return render_template('add_staff.html', user_role= user_role, username=session['username'])
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login'))
    

@app.route("/admin/marinerlist")
def adminMarinerList():
    if "loggedin" in session and session["user_role"] == "admin":
        return marinerList()   
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login')) 
    
@app.route("/admin/guidelist")
def adminGuideList():
    if "loggedin" in session and session["user_role"] == "admin":
        return guideList()  
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login')) 
    
    
@app.route("/admin/guide/add", methods=["GET", "POST"])
def adminAddGuide():
    if "loggedin" in session and session["user_role"] == "admin":
        return addGuide()
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login'))