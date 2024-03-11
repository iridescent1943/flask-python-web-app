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
from app.shared import changePassword
from app.shared import guideDetails


@app.route("/user/home")
def marinerHome():
    if "loggedin" in session and session["user_role"] == "admin":
        return redirect("/admin/home")
    elif "loggedin" in session and session["user_role"] == "staff":
        return redirect("/staff/home")
    elif "loggedin" in session and session["user_role"] == "mariner":
        return home()
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login'))
    
    
@app.route("/user/profile", methods=["GET"])
def marinerProfile(): 
    if "loggedin" in session and session["user_role"] == "admin":
        return redirect("/admin/profile")
    elif "loggedin" in session and session["user_role"] == "staff":
        return redirect("/staff/profile")
    elif "loggedin" in session and session["user_role"] == "mariner":
        user_id = session.get('user_id')
        cursor = getCursor()
        sql = """
        SELECT username, first_name, last_name, email, phone, address, date_joined
        FROM user INNER JOIN mariner
        ON user.user_id = mariner.user_id
        WHERE user.user_id = %s;
        """
        cursor.execute(sql, (user_id,))
        PROFILE = cursor.fetchone()
        return render_template('mariner_profile.html', user_role= session['user_role'], username=session['username'], profile=PROFILE)
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login'))
    

@app.route("/user/profile/edit", methods=["GET", "POST"])
def editMarinerProfile():    
    if "loggedin" in session and session["user_role"] == "admin":
        return redirect("/admin/profile/edit")
    elif "loggedin" in session and session["user_role"] == "staff":
        return redirect("/staff/profile/edit")
    elif "loggedin" in session and session["user_role"] == "mariner": 
        user_id = session.get('user_id')
        cursor = getCursor()
        # Fetch mariner profile details        
        sql1 = """
        SELECT first_name, last_name, email, phone, address
        FROM user INNER JOIN mariner
        ON user.user_id = mariner.user_id
        WHERE user.user_id = %s;
        """
        cursor.execute(sql1, (user_id,))
        PROFILE = cursor.fetchone()
        # if the user sends the request to update the profile details
        if request.method == "POST":
            first_name = request.form.get("first_name")
            last_name = request.form.get("last_name")
            email = request.form.get("email")
            phone = request.form.get("phone")
            address = request.form.get("address")
            sql2 = """
            UPDATE mariner
            SET first_name = %s, last_name = %s, email = %s, phone = %s, address = %s
            WHERE user_id = %s;
            """
            cursor.execute(sql2, (first_name, last_name, email, phone, address, user_id))
            return redirect(url_for('marinerProfile'))
        else:
            return render_template('mariner_profile_edit.html', user_role= session['user_role'], username=session['username'], profile=PROFILE)
    else: 
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login'))


@app.route("/user/changepassword", methods=["GET", "POST"])
def marinerChangePassword(): 
    if "loggedin" in session and session["user_role"] == "admin":
        return redirect("/admin/changepassword")
    elif "loggedin" in session and session["user_role"] == "staff":
        return redirect("/staff/changepassword")
    elif "loggedin" in session and session["user_role"] == "mariner":    
        return changePassword()
    else: 
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login'))
    

@app.route("/user/guidedetails/<guide_id>")
def userGuideDetails(guide_id): 
    if "loggedin" in session and session["user_role"] == "admin":
        return redirect(f"/admin/guidedetails/{guide_id}")
    elif "loggedin" in session and session["user_role"] == "staff":
        return redirect(f"/staff/guidedetails/{guide_id}")
    elif "loggedin" in session and session["user_role"] == "mariner":    
        return guideDetails(guide_id)
    else: # User is not loggedin, redirect to login page
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login'))


