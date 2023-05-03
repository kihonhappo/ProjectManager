## Simple Project Management Web App

# Overview

{Important!  Do not say in this section that this is college assignment.  Talk about what you are trying to accomplish as a software engineer to further your learning.}

{Provide a description the web app that you wrote. Describe how to start a test server on your computer and what website to open up to see the first page of the app.}

{Describe your purpose for writing this software.}

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (starting the server and navigating through the web pages) and a walkthrough of the code.}

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
10. Install psycopg2-binary - pip install psycopg2-binary
11. Install Django Rest Framework - pip install djangorestframework
12. Create Front-End App - python manage.py startapp main
13. Models - When you create/change/delete a model use this cmd to update chages - python manage.py makemigrations
14. Install Node JS - https://nodejs.org/en
15. Install React Front-End - npm create-react-app front-end
16. Install Bootstrap 5 

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
* [PostgreSQL](https://www.postgresql.org)
* [PgAdmin](https://www.pgadmin.org/)
* [NodeJS](https://nodejs.org/en)
* [React JS](https://react.dev/)
* [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

# Future Work

* User authentication
* JWT token authorization for API consumers
* Multilingual 