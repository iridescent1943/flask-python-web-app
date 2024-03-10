
# Biosecurity Guide 

##### COMP639 Assignment 1 WebApp

#####  *Submitted by Hannah Chen*

##

## Section 1: A Short Introduction

> This web application provides a single login system for 3 different types of users, including admin, staff and mariners. Once logged in, the user will be taken to a tailored home page with a tailored dashboard, so that the user can only access the routes and perform the actions relevant to the user role, to ensure data safety and integrity. 

***The admin*** has the highest level of access. The admin can manage staff, mariners and guides.

***The staff*** has the second highest level of access and can manage mariners and guides. 

***The mariner*** can only view guides contents. 

***All users*** can manage their own account, including updating personal profile information and changing password.

## Section 2: About Some Features

***login:*** existing users can log in by providing correct username and password, the password is hidden when the user is typing. This app does not support "show password" feature on the login page.

***register:*** new mariner users can create an accounts for themselves through the register feature on the login page. staff accounts need to be created by the admin.

***Sources page:*** A footer section is added to the guide detail page so the mariner users can check the references if needed.

***Image upload:*** The app only support the upload of image with a english name at this stage.

## Section 3 Data Model
 <img src="biosecurity\static\img\database_structure.png" alt="database_structure" align=center />

**Notes:**
1. one user id can only correspond to either one mariner or one staff (admin is also a staff)
2. one guide can have many images.