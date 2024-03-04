from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import flash

from app import app
from flask_hashing import Hashing
hashing = Hashing(app)

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


@app.route("/staff/home")
def staffHome():
    if "loggedin" in session and session["user_role"] == "admin":
        return redirect("/admin/home")
    elif "loggedin" in session and session["user_role"] == "staff":
        return home()
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login'))
    

@app.route("/staff/profile", methods=["GET"])
def staffProfile():    
    if "loggedin" in session and session["user_role"] == "admin":
        return redirect("/admin/profile")
    elif "loggedin" in session and session["user_role"] == "staff":
        return adminOrStaffProfile()
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login'))


@app.route("/staff/profile/edit", methods=["GET", "POST"])
def editStaffProfile():    
    if "loggedin" in session and session["user_role"] == "admin":
        return redirect ("/admin/profile/edit")
    elif "loggedin" in session and session["user_role"] == "staff":
        return editAdminOrStaffProfile()
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login'))
    

@app.route("/staff/changepassword", methods=["GET", "POST"])
def staffChangePassword():    
    if "loggedin" in session and session["user_role"] == "admin":
        return redirect(url_for("/admin/changepassword"))
    elif "loggedin" in session and session["user_role"] == "staff":
        return changePassword()
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login'))
    

@app.route("/staff/marinerlist")
def staffMarinerList():
    if "loggedin" in session and session["user_role"] == "admin":
        return redirect("/admin/marinerlist")
    elif "loggedin" in session and session["user_role"] == "staff":
        return marinerList()  
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login'))
    

@app.route("/staff/mariner/edit/<mariner_id>", methods=["GET", "POST"])
def staffEditMariner(mariner_id):
    if "loggedin" in session and session["user_role"] == "admin":
        return redirect("/admin/mariner/edit/<mariner_id>")    
    if "loggedin" in session and session["user_role"] == "staff":
        return adminOrStaffEditMariner(mariner_id)
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login'))
    

@app.route("/staff/mariner/inactivate/<mariner_id>", methods=["GET", "POST"])
def staffInactivateMariner(mariner_id): 
    if "loggedin" in session and session["user_role"] == "admin":
        return redirect("/admin/mariner/inactivate/<mariner_id>")
    if "loggedin" in session and session["user_role"] == "staff":
        return inactivateMariner(mariner_id)
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login')) 
    

@app.route("/staff/mariner/reactivate/<mariner_id>", methods=["GET", "POST"])
def staffReactivateMariner(mariner_id): 
    if "loggedin" in session and session["user_role"] == "admin":
        return redirect("/admin/mariner/reactivate/<mariner_id>")
    if "loggedin" in session and session["user_role"] == "staff":
        return reactivateMariner(mariner_id)
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login')) 
    
    
@app.route("/staff/mariner/delete/<user_id>", methods=["GET", "POST"])
def staffDeleteMariner(user_id):
    if "loggedin" in session and session["user_role"] == "admin":
        return redirect("/admin/mariner/delete/<user_id>")
    if "loggedin" in session and session["user_role"] == "staff":
        return deleteMariner(user_id)
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login')) 

    
    
@app.route("/staff/guidelist")
def staffGuideList():
    if "loggedin" in session and session["user_role"] == "admin":
        return redirect("/admin/guidelist")
    elif "loggedin" in session and session["user_role"] == "staff":
        return guideList()
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login'))
    

@app.route("/staff/guide/add", methods=["GET", "POST"])
def staffAddGuide():
    if "loggedin" in session and session["user_role"] == "admin":
        return redirect("/admin/guide/add")
    elif "loggedin" in session and session["user_role"] == "staff":
        return addGuide()
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login'))
    

@app.route("/staff/guidedetails/<ocean_id>", methods=["GET", "POST"])
def staffGuideDetails(ocean_id):
    if "loggedin" in session and session["user_role"] == "admin":
        return redirect("/admin/guidedetails/<ocean_id>")
    elif "loggedin" in session and session["user_role"] == "staff":
        return guideDetails(ocean_id)
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login'))   

    

@app.route("/staff/guide/edit/<ocean_id>", methods=["GET", "POST"])
def staffEditGuide(ocean_id):
    if "loggedin" in session and session["user_role"] == "admin":
        return redirect("/admin/guide/edit/<ocean_id>")
    elif "loggedin" in session and session["user_role"] == "staff":
        return editGuideDetails(ocean_id)
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login'))
    

@app.route("/staff/guide/delete/<ocean_id>", methods=["GET", "POST"])
def staffDeleteGuide(ocean_id):
    if "loggedin" in session and session["user_role"] == "admin":
        return redirect("/admin/guide/delete/<ocean_id>")
    elif "loggedin" in session and session["user_role"] == "staff":
        return deleteGuide(ocean_id)
    else:
        flash("Authorized users only. Please log in.", "error")
        return redirect(url_for('login'))