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
from app.shared import inactivateMariner
from app.shared import reactivateMariner
from app.shared import deleteMariner
from app.shared import adminOrStaffEditMariner
from app.shared import guideDetails
from app.shared import editGuideDetails
from app.shared import deleteGuide


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
            user_role = "staff"
            first_name = request.form.get("first_name")
            last_name = request.form.get("last_name")            
            department = request.form.get("department")
            position = request.form.get("position")
            work_phone = request.form.get("work_phone")            
            hire_date = request.form.get("hire_date")
            email = request.form.get("email")
            
            # Check if the entered username already exists in the database
            sql1 = "SELECT * FROM user WHERE username = %s;"
            cursor.execute(sql1, (username,))
            ACCOUNT = cursor.fetchone()
            if ACCOUNT is not None:
                return "Username already exists. Please choose a different username."
            else:
                # Username is available, continue to register the staff            
                sql2 = """
                    START TRANSACTION;
                    INSERT INTO user (username, password, user_role) 
                    VALUES (%s, %s, %s);
                    INSERT INTO staff (user_id, first_name, last_name, email, work_phone, department, position, hire_date)
                    VALUES (LAST_INSERT_ID(), %s, %s, %s, %s, %s, %s, %s);
                    commit;
                    """
                cursor.execute(sql2, (username, hashed_password, user_role, first_name, last_name, email, work_phone, department, position, hire_date))
                flash ("Staff added successfully.", "success")      
                return redirect(url_for('staffList'))
        else:
            return render_template('add_staff.html', user_role= user_role, username=session['username'])
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login'))
    

@app.route("/admin/staff/edit/<staff_id>", methods=["GET", "POST"])
def editStaff(staff_id):
    if 'loggedin' in session and session["user_role"] == "admin":
        cursor = getCursor()            
        sql1 = """
        SELECT first_name, last_name, email, work_phone, department, position, hire_date
        FROM staff
        WHERE staff_id = %s;
        """
        cursor.execute(sql1, (staff_id,))
        PROFILE = cursor.fetchone()    
        if request.method == "POST":
            first_name = request.form.get("first_name")
            last_name = request.form.get("last_name")
            email = request.form.get("email")
            work_phone = request.form.get("work_phone")
            department = request.form.get("department")
            position = request.form.get("position")
            hire_date = request.form.get("hire_date")
            sql2 = """
            UPDATE staff
            SET first_name = %s, last_name = %s, email = %s, work_phone = %s, department = %s, position = %s, hire_date = %s
            WHERE staff_id = %s;
            """
            cursor.execute(sql2, (first_name, last_name, email, work_phone, department, position, hire_date, staff_id))
            flash("Staff details updated successfully.", "success")
            return redirect(url_for('staffList'))
        else:
            return render_template('staff_profile_edited_by.html', user_role = session["user_role"], username=session['username'], profile=PROFILE, staff_id=staff_id)
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login'))



@app.route("/admin/staff/inactivate/<staff_id>", methods=["GET", "POST"])
def inactivateStaff(staff_id):    
    if 'loggedin' in session and session["user_role"] == "admin":
        if request.method == "POST":
            cursor = getCursor()
            sql = """
            UPDATE staff
            SET active_user = 0
            WHERE staff_id = %s;
            """
            cursor.execute(sql, (staff_id,))
            flash("Staff account inactivated successfully.", "success")
            return redirect(url_for('staffList'))  
        else:
            return redirect(url_for('staffList'))        
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login'))
    

@app.route("/admin/staff/reactivate/<staff_id>", methods=["GET", "POST"])
def reactivateStaff(staff_id):    
    if 'loggedin' in session and session["user_role"] == "admin":
        if request.method == "POST":
            cursor = getCursor()
            sql = """
            UPDATE staff
            SET active_user = 1
            WHERE staff_id = %s;
            """
            cursor.execute(sql, (staff_id,))
            flash("Staff account reactivated successfully.", "success")
            return redirect(url_for('staffList'))  
        else:
            return redirect(url_for('staffList'))        
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login'))
    

@app.route("/admin/staff/delete/<user_id>", methods=["GET", "POST"])
def deleteStaff(user_id):    
    if 'loggedin' in session and session["user_role"] == "admin":
        if request.method == "POST":
            cursor = getCursor()
            sql = "DELETE FROM user WHERE user_id = %s;"
            cursor.execute(sql, (user_id,))
            flash("Staff account deleted successfully.", "success")
            return redirect(url_for('staffList'))  
        else:
            return redirect(url_for('staffList'))        
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
    

@app.route("/admin/mariner/edit/<mariner_id>", methods=["GET", "POST"])
def adminEditMariner(mariner_id):
    if "loggedin" in session and session["user_role"] == "admin":
        return adminOrStaffEditMariner(mariner_id) 
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login'))
    

@app.route("/admin/mariner/inactivate/<mariner_id>", methods=["GET", "POST"])
def adminInactivateMariner(mariner_id): 
    if "loggedin" in session and session["user_role"] == "admin":
        return inactivateMariner(mariner_id)
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login')) 


@app.route("/admin/mariner/reactivate/<mariner_id>", methods=["GET", "POST"])
def adminReactivateMariner(mariner_id): 
    if "loggedin" in session and session["user_role"] == "admin":
        return reactivateMariner(mariner_id)
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login')) 
    
    
@app.route("/admin/mariner/delete/<user_id>", methods=["GET", "POST"])
def adminDeleteMariner(user_id): 
    if "loggedin" in session and session["user_role"] == "admin":
        return deleteMariner(user_id)
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
    

@app.route("/admin/guidedetails/<ocean_id>", methods=["GET", "POST"])
def adminGuideDetails(ocean_id):
    if "loggedin" in session and session["user_role"] == "admin":
        return guideDetails(ocean_id)
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login'))
       

@app.route("/admin/guide/edit/<ocean_id>", methods=["GET", "POST"])
def adminEditGuide(ocean_id):
    if "loggedin" in session and session["user_role"] == "admin":
        return editGuideDetails(ocean_id)
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login'))


@app.route("/admin/guide/delete/<ocean_id>", methods=["GET", "POST"])
def adminDeleteGuide(ocean_id):
    if "loggedin" in session and session["user_role"] == "admin":
        return deleteGuide(ocean_id)
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login'))

