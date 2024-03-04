from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import flash
from flask_hashing import Hashing
from app import app
hashing = Hashing(app)

import mysql.connector
from mysql.connector import FieldType
import connect as connect

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


def home():  
    PEST_IN_NZ, DISEASE_IN_NZ, PEST_NOT_IN_NZ, DISEASE_NOT_IN_NZ = getGuideImageList()
    return render_template("home.html", user_role = session["user_role"], username=session['username'], pest_in_nz=PEST_IN_NZ, disease_in_nz=DISEASE_IN_NZ, pest_not_in_nz=PEST_NOT_IN_NZ, disease_not_in_nz=DISEASE_NOT_IN_NZ)


def adminOrStaffProfile(): 
    user_id = session.get('user_id')
    cursor = getCursor()
    sql = """
    SELECT username, first_name, last_name, email, work_phone, department, position, hire_date
    FROM user INNER JOIN staff
    ON user.user_id = staff.user_id
    WHERE user.user_id = %s;
    """
    cursor.execute(sql, (user_id,))
    PROFILE = cursor.fetchone()
    return render_template('staff_profile.html', user_role = session["user_role"], username=session['username'], profile=PROFILE)

  
def editAdminOrStaffProfile():  
    user_id = session.get('user_id')
    cursor = getCursor()            
    sql1 = """
    SELECT first_name, last_name, email, work_phone, department, position, hire_date
    FROM user INNER JOIN staff
    ON user.user_id = staff.user_id
    WHERE user.user_id = %s;
    """
    cursor.execute(sql1, (user_id,))
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
        WHERE user_id = %s;
        """
        cursor.execute(sql2, (first_name, last_name, email, work_phone, department, position, hire_date, user_id))
        return redirect(url_for('staffProfile'))
    else:
        return render_template('staff_profile_edit.html', user_role = session["user_role"], username=session['username'], profile=PROFILE)



def changePassword():    
    user_id = session.get('user_id')        
    cursor = getCursor()            
    if request.method == "POST":
        old_password = request.form.get("old_password")
        new_password = request.form.get("new_password")            
        # Check if the old password is correct
        sql1 = "SELECT password FROM user WHERE user_id = %s;"
        cursor.execute(sql1, (user_id,))
        PASSWORD = cursor.fetchone()
        if hashing.check_value(PASSWORD[0], old_password, salt='rainbow'):
            # If the old password is correct, update the password
            hashed_password = hashing.hash_value(new_password, salt='rainbow')
            sql2 = "UPDATE user SET password = %s WHERE user_id = %s;"
            cursor.execute(sql2, (hashed_password, user_id))
            flash('Password changed successfully. Please log in with new password.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Old password is incorrect. Please try again.', 'error')
            return render_template('change_password.html', user_role = session["user_role"], username=session['username'],user_id = user_id)
    else:
        return render_template('change_password.html', user_role = session["user_role"], username=session['username'], user_id = user_id)


def marinerList():
    cursor = getCursor()
    sql = "SELECT * FROM mariner"
    cursor.execute(sql)
    MARINERS = cursor.fetchall()
    return render_template('mariner_list.html', user_role = session["user_role"], username=session['username'], mariners=MARINERS)


def adminOrStaffEditMariner(mariner_id):    
    cursor = getCursor()            
    sql1 = """
    SELECT first_name, last_name, email, phone, address
    FROM mariner    
    WHERE mariner_id = %s;
    """
    cursor.execute(sql1, (mariner_id,))
    PROFILE = cursor.fetchone()
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        address = request.form.get("address")
        sql2 = """
        UPDATE mariner
        SET first_name = %s, last_name = %s, email = %s, phone = %s, address = %s
        WHERE mariner_id = %s;
        """
        cursor.execute(sql2, (first_name, last_name, email, phone, address, mariner_id))
        if session["user_role"] == "admin":
            return redirect(url_for('adminMarinerList'))
        else:
            return redirect(url_for('staffMarinerList'))
    else:
        return render_template('mariner_profile_edited_by.html', user_role= session['user_role'], username=session['username'], profile=PROFILE, mariner_id=mariner_id)


def inactivateMariner(mariner_id):   
    cursor = getCursor()
    sql = """
    UPDATE mariner
    SET active_user = 0
    WHERE mariner_id = %s;
    """
    cursor.execute(sql, (mariner_id,))
    if session["user_role"] == "admin":
        return redirect(url_for('adminMarinerList'))
    else: 
        return redirect(url_for('staffMarinerList'))


def reactivateMariner(mariner_id):   
    cursor = getCursor()
    sql = """
    UPDATE mariner
    SET active_user = 1
    WHERE mariner_id = %s;
    """
    cursor.execute(sql, (mariner_id,))
    if session["user_role"] == "admin":
        return redirect(url_for('adminMarinerList'))
    else: 
        return redirect(url_for('staffMarinerList'))


def deleteMariner(user_id):   
    cursor = getCursor()
    sql = "DELETE FROM user WHERE user_id = %s;"
    cursor.execute(sql, (user_id,))
    if session["user_role"] == "admin":
        return redirect(url_for('adminMarinerList'))
    else:
        return redirect(url_for('staffMarinerList'))


def guideList():    
    cursor = getCursor()
    sql = """
    SELECT guide.ocean_id, common_name, scientific_name, ocean_item_type, present_in_NZ, description, threats, key_characteristics, location, image_url
    FROM guide INNER JOIN image
    ON guide.ocean_id = image.ocean_id;
    """
    cursor.execute(sql)
    GUIDES = cursor.fetchall()
    return render_template('guide_list.html', user_role = session["user_role"], username=session['username'], guides=GUIDES)


def addGuide():
    cursor = getCursor()
    if request.method == "POST":
        common_name = request.form.get("common_name")
        scientific_name = request.form.get("scientific_name")
        ocean_item_type = request.form.get("ocean_item_type")
        present_in_NZ = request.form.get("present_in_NZ")
        description = request.form.get("description")
        threats = request.form.get("threats")
        key_characteristics = request.form.get("key_characteristics")
        location = request.form.get("location")
        image_url = request.form.get("image_url")
        sql1 = "INSERT INTO guide (common_name, scientific_name, ocean_item_type, present_in_NZ, description, threats, key_characteristics, location) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
        cursor.execute(sql1, (common_name, scientific_name, ocean_item_type, present_in_NZ, description, threats, key_characteristics, location))
        ocean_id = cursor.lastrowid
        sql2 = "INSERT INTO image (ocean_id, image_url, primary_image) VALUES (%s, %s, 0);"
        cursor.execute(sql2, (ocean_id, image_url))
        if session["user_role"] == "admin":
            return redirect(url_for('adminGuideList'))
        else:
            return redirect(url_for('staffGuideList'))
    else:
        return render_template('add_guide.html',user_role = session["user_role"], username=session['username'])
    

def getGuideImageList():
        cursor = getCursor()
        sql1 = """
        SELECT guide.ocean_id, common_name, present_in_NZ, image_url 
        FROM guide 
        INNER JOIN image
        ON guide.ocean_id = image.ocean_id
        WHERE guide.ocean_item_type = 'pest' AND guide.present_in_NZ = 'yes' AND image.primary_image = 1;     
        """   
        cursor.execute(sql1)
        PEST_IN_NZ = cursor.fetchall()

        sql2 = """
        SELECT guide.ocean_id, common_name, present_in_NZ, image_url
        FROM guide
        INNER JOIN image
        ON guide.ocean_id = image.ocean_id
        WHERE guide.ocean_item_type = 'disease' AND guide.present_in_NZ = 'yes' AND image.primary_image = 1;     
        """
        cursor.execute(sql2)
        DISEASE_IN_NZ = cursor.fetchall()

        sql3 = """
        SELECT guide.ocean_id, common_name, present_in_NZ, image_url
        FROM guide
        INNER JOIN image
        ON guide.ocean_id = image.ocean_id
        WHERE guide.ocean_item_type = 'pest' AND guide.present_in_NZ = 'no' AND image.primary_image = 1;     
        """
        cursor.execute(sql3)
        PEST_NOT_IN_NZ = cursor.fetchall()

        sql4 = """
        SELECT guide.ocean_id, guide.common_name, guide.present_in_NZ, image.image_url
        FROM guide
        INNER JOIN image
        ON guide.ocean_id = image.ocean_id
        WHERE guide.ocean_item_type = 'disease' AND present_in_NZ = 'no' AND image.primary_image = 1;     
        """
        cursor.execute(sql4)
        DISEASE_NOT_IN_NZ = cursor.fetchall()
        return PEST_IN_NZ, DISEASE_IN_NZ, PEST_NOT_IN_NZ, DISEASE_NOT_IN_NZ


def guideDetails(ocean_id):   
    cursor = getCursor()
    sql = """
    SELECT guide.common_name, guide.scientific_name, guide.ocean_item_type, guide.present_in_NZ, guide.description, guide.threats, guide.key_characteristics, guide.location, image.image_url
    FROM guide
    INNER JOIN image ON guide.ocean_id = image.ocean_id
    WHERE guide.ocean_id = %s;
    """
    cursor.execute(sql, (ocean_id,))
    GUIDE = cursor.fetchone()
    return render_template('guide_details.html', user_role= session['user_role'], username=session['username'], guide=GUIDE)

    
def editGuideDetails(ocean_id):
    cursor = getCursor()
    sql1 = "SELECT * FROM guide WHERE ocean_id = %s;"
    cursor.execute(sql1, (ocean_id,))
    GUIDE = cursor.fetchone()
    sql2 = "SELECT * FROM image WHERE ocean_id = %s;"
    cursor.execute(sql2, (ocean_id,))
    IMAGES = cursor.fetchall()
    if request.method == "POST":
        common_name = request.form.get("common_name").capitalize()
        scientific_name = request.form.get("scientific_name").capitalize()
        ocean_item_type = request.form.get("ocean_item_type")
        present_in_NZ = request.form.get("present_in_NZ")
        description = request.form.get("description")
        threats = request.form.get("threats")
        key_characteristics = request.form.get("key_characteristics")
        location = request.form.get("location")
        primary_image = request.form.get("primary_image")
        sql3 = """
        UPDATE guide
        SET common_name = %s, scientific_name = %s, ocean_item_type = %s, present_in_NZ = %s, description = %s, threats = %s, key_characteristics = %s, location = %s
        WHERE ocean_id = %s;
        """
        cursor.execute(sql3, (common_name, scientific_name, ocean_item_type, present_in_NZ, description, threats, key_characteristics, location, ocean_id))
        sql4 = """
            START TRANSACTION;
            UPDATE image
            SET primary = 1
            WHERE ocean_id = %s and image_url = %s;
            Set primary = 0
            WHERE ocean_id = %s and image_url != %s;
            COMMIT;
            """
        cursor.execute(sql4, (ocean_id, primary_image, ocean_id, primary_image))
        if session["user_role"] == "admin":
            return redirect(url_for('adminGuideDetails', ocean_id=ocean_id))
        else:
            return redirect(url_for('staffGuideDetails', ocean_id=ocean_id))
    else:
        return render_template('edit_guide.html', user_role = session["user_role"], username=session['username'], guide=GUIDE, images=IMAGES)


def deleteGuide(ocean_id):   
    cursor = getCursor()    
    sql = "DELETE FROM guide WHERE ocean_id = %s;"
    cursor.execute(sql, (ocean_id,))
    if session["user_role"] == "admin":
        return redirect(url_for('adminGuideList'))
    else:
        return redirect(url_for('staffGuideList'))