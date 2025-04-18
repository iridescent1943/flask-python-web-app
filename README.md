## A Short Introduction

> This web application provides information on ocean pests and diseases present in New Zealand. It includes a single login system for 3 different types of users, including admin, staff and mariners. Once logged in, the user will be taken to a tailored home page with a tailored dashboard, so that the user can only access the routes and perform the actions relevant to the user role, to ensure data safety and integrity. 

**The admin** has the highest level of access. The admin can manage staff, mariners and guides.

**The staff** has the second highest level of access and can manage mariners and guides. 

**The mariner** can only view guides contents. 

**All users** can manage their own account, including updating personal profile information and changing password.

## About Some Features

**login:** existing users can log in by providing correct username and password, the password is hidden when the user is typing. This web app currently does not support "show password" feature on the login page.

> Note that if a user is already logged in, when the user revisits the login page, the user will be redirected to corresponding home page, without the need to enter username and password again. This web app does not support auto logout feature at this stage.

**register:** new mariner users can create an accounts for themselves through the register feature on the login page. staff accounts need to be created by the admin.

**sources page:** A footer section is added to the guide detail page so the mariner users can check the references if needed.

**staff list:** While the admin is also a staff, when the admin access the staff list, the admin itself is not shown in the list to avoid accidental deactivation. Also, it is not necessary to include the admin in the staff list as the admin can update its account information through *manage profile* and *change password* features.

**add guide:** It is assumed that the common name and scientific name of a pest or a disease might contain special characters, therefore not just alphabetic letters are allowed in the common or scientific names. 

**upload image:** The app only support the upload of image with a English name at this stage.

**delete image:** When the admin/staff delete a image from a guide, the image will also be deleted from the folder, as it is assumed that different guides would not share the same image and it might not be good to keep the image in the folder when the image is no longer needed. Therefore, to test if the delete image feature work, better to upload a new image then delete it. The *app\static\img - backup* folder contains all original images. 

## Entity-Relationship Model
 <img src="app\static\img\database_structure.png" alt="database_structure" align=center />

**Notes:**
1. one user id can only correspond to either one mariner or one staff (admin is also a staff). One mariner or one staff can only have one user id. 
2. one guide can have one or many images. One image can only have one ocean id. 
3. the *mariner* and *staff* tables are linked to the *user* table via foreign key *user_id*.

## Some Screenshots of the Web App
<img src="app\static\login.png" alt="login_page" align=center style="margin-bottom: 20px;" />

<img src="app\static\homepage.png" alt="home_page" align=center style="margin-bottom: 20px;" />

<img src="app\static\dashboard.png" alt="dashboard_page" align=center style="margin-bottom: 20px;" />

<img src="app\static\logout.png" alt="logout_page" align=center style="margin-bottom: 20px;" />

<img src="app\static\new_staff.png" alt="new_staff_page" align=center style="margin-bottom: 20px;" />