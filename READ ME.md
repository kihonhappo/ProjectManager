## Simple Project Management Web App

# Overview

The Simple Project Mangement Web App is set up to allow users to create, track and improve existing and future projects.
Phase 1 is meant to be used by a single person on a local device. 
Phase 2 could integrate with Google Suite 
Phase 3 could seperate the backend Django api from the front-end React app from the Postgres DB. All three parts can then be moved to the cloud.

# Startup the Backend Django API Webserver
After installing Python and Django you start your web server using this command - python manage.py runserver
Open your browser and navigate to http://127.0.0.1:8000/api/ for the client api page or navigate to http://127.0.0.1:8000/admin/ for the Django admin website. Please refer to the Setup project and Create database models for a more detailed set of steps for setting up your backend project.
# Startup the Front-end React Nodejs application Server
After installing Node and React you start your applicaiton server using this command - npm start
Open your web browser and naviagte to http://localhost:3000/ for the front-end client React App. This app consumes the Django client apis.
Please refer to the Setup project and Create database models for a more detailed set of steps for setting up your front-end Applicaiton.

# Purpose

I wrote this software to demonstrate how to use Django as a web api that can then be consumed by a seperate front-end web application. Project or Task management is an esential tool that can be used by anyone who has to complete simple or complex, multistep activities. 

# Softwar Demo Video Walkthrough

[Software Demo Video](http://youtube.link.goes.here)

# Web Pages

-----------------------------------------------------------
- Website
    - Dashboard
        -   Header
        -   Select Projects Drop Down
        -   Selected Project Backlog Items Drop Down
        -   Selected Work Events
        -   Selected Project Kanban Board
        -   Footer
==========================================================
-   Project Manager Panel
    -   Projects List
        -   List View (Table Format)
        -   New Project Input Form
        -   Edit Existing Project Form
        -   Delete Project
        -   Pagination
    -   Backlog Items List
        -   List View (Table Format)
        -   New Backlog Item Input Form
        -   Edit Existing Backlog Item Form
        -   Delete Backlog Item
        -   Pagination
    -   Work Event List
        -   List View (Table Format)
        -   New Work Event Input Form
        -   Edit Existing Work Event Form
        -   Delete Work Event
        -   Pagination
    -   Stakeholders List
        -   List View (Table Format)
        -   New Stakeholders Input Form
        -   Edit Existing Stakeholders Form
        -   Delete Stakeholders
        -   Pagination
======================================================
-   Admin Panel
    -   User Manager
        -   User Groups
        -   View Level
        -   List View
        -   New User Input Form
        -   Edit User Input Form
        -   Delete User
    -   Database Analyzer
        -   Data Model Builder
        -   Table Analyzer
        -   Column Analyser

# Development Environment (2023)
------------------------------------------
-   Visual Studio Code (VSCode)
-   Notepad ++

# Technologies (2023)
-   Python 3.9.4
-   Django 
-   ReactJs - 18.2
-   Bootstrap 5.2
-   Postgresql  15.2
-   pgAdmin 4
-   Windows 11

# Setup project and Create database models
1.  Install Python - https://www.python.org/
2.  Install Virtual Environment - pip install virtualenv
3.  Create Virtual Environment - python -m venv venv
4.  Activate Virtual Environment: (Windows - cmd: venv\Scripts\activate.bat, ps: venv\Scripts\Activate.ps1) (Linus: source env/bin/activate)
5.  Install Django - pip install django
6.  Create Django Project - django-admin startproject backend_api
7.  Run Django Project - python manage.py runserver
8.  Install PostgreSQL - https://www.postgresql.org/docs/
9.  Install pgAdmin - https://www.pgadmin.org/
10. Install psycopg2-binary - pip install psycopg2-binary - This is the Postgres driver for Django
11. Install Django Rest Framework - pip install djangorestframework
12. Create Front-End App - python manage.py startapp main
13. Models - When you create/change/delete a model use this cmd to update chages - python manage.py makemigrations
14. Install Node JS - https://nodejs.org/en
15. Install React Front-End - npm create-react-app front-end
16. Install Bootstrap 5 
17. Run node application server - navigate to your React app directory, mine is front-end. Then use this command - npm start

# Models

-   Project
    -   Title
    -   Description
    -   Start_Date
    -   End_Date
    -   Life_Cycle
    -   Status
    -   Owner
    -   Created
    -   Created_By
    -   Modified
    -   Modified_By  

-   Backlog Item
    -   Title
    -   Project
    -   Description
    -   Projected_Hours
    -   Actual_Hours
    -   Start_Date
    -   End_Date
    -   Assigned_To
    -   Plan
    -   Status
    -   Created
    -   Created_By
    -   Modified
    -   Modified_By

-   Work Event
    -   Title
    -   Project
    -   Backlog_Item
    -   Worker
    -   Work_Date
    -   Start_Time
    -   End_Time
    -   Duration
    -   Work_Performed
    -   Next_Steps
    -   Created
    -   Created_By
    -   Modified
    -   Modified_By

-   Stakeholder
    -   First_Name
    -   Last_Name
    -   Company
    -   Title
    -   Email
    -   Phone
    -   Gender
    -   Ethnicity
    -   User
    -   Created
    -   Created_By
    -   Modified
    -   Modified_By

-   Assignments
    -   Project
    -   Stakeholder
    -   Role
    -   Assignment_Date
    -   Created
    -   Created_By
    -   Modified
    -   Modified_By

-   Staus
    -   Title
    -   Description

-   Lifecycle
    -   Title
    -   Description

# Useful Websites

* [VSCode](https://code.visualstudio.com/)
* [Notpad++](https://notepad-plus-plus.org/)
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Django Rest Framework](https://www.django-rest-framework.org)
* [Django Rest Framework Router](https://www.django-rest-framework.org/api-guide/routers/)
* [PostgreSQL](https://www.postgresql.org)
* [PgAdmin](https://www.pgadmin.org/)
* [NodeJS](https://nodejs.org/en)
* [React JS](https://react.dev/)
* [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

## Future Work

# Backend

* User authentication
* JWT token authorization for API consumers
* Multilingual 
* Google Suite Integration

# Frontend
- User Management 
    - Login Form
    - Registration Form
    - Profile Form
    - Admin dashboard
- Listview
    - Add create new record 
    - Add edit record
    - Add delete record
    - Add copy record
    - Add batch process checkbox for delete and copy record
    - Add sort by
    - Add serach filter
    - Add hide/show columns
    - Add Export functions - .csv, .json, .xml, .text
- Add record details form
    - Edit record
    - View record
    - New record
- Visualizatio Boards
    - Kanban
    - LifeCycle
    - Scrum
- Google Suite Integration
    - Calendar
    - Tasks
    - Drive

