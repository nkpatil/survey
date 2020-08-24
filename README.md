# Dynamic Survey Form

This is a survey builder web application developed using Django. People can use this to generate the forms dynamically and share with others to fill the survey. Also there is an option to download the generated form as JSON so that the same can be used in the future to clone the same form.


# UX / UI

Beautification of UI is not yet implemented. Few validations are already applied but still there is a scope of implementing more validations and error handling.
For fill survey page, wizard like panel can be used to fill the data section wise and one section will be shown at a time. Every section will have button called "Next" and user will be keep filling the form until all the sections are covered.
For form building (generating sections and questions dynamically), drag drop can be used to move up/down to set the order.
Show survey page will have to be improved like format need to be fixed and option to download the data needs to be provided.

Sections are movable, you can drag and move the section up and down and it will set order accordingly.

## Other UI Improvements

Lot of components are similar and used at multiple places, which can be generalised and put into some utils and can be used anywhere.
React JS can be used for better UI components handling.
Code has to be improved to generate the different inputs, most of the parameters are usually same in all different type of inputs.

Pages:
- To generate survey form: http://localhost:8000/
- To show the filled responses: http://localhost:8000/survey_answers/
- To fill the survey form: http://localhost:8000/fill_survey/4

All above pages are using the same base (base.html) which has header, footer, menu etc common in all the pages.

## Database

- Survey : Table survey to store survey details along with created user. Fields are: name, description, user, time
- Section: Section table will store multiple sections under a survey which will then contain multiple questions. Fields: survey_id, name, description, order.
- Question: To store questions and their details. Questions are connected to sections using foreign key and stores section_id, title, description, input_type, input length, required, order, options(comma separated values).
- Answer: To store answers filled by uses. Fields: question_id, text (answer), user, submitted_at.


## Frameworks and tools used
- Backend: Django, python, postgresql
- Deployment: Heroku
- Frontend: HTML, css, javascript, jquery, ajax, bootstrap


## Local Installation and Setup
(Install python-pip and setup a virtual environment)
- git clone https://github.com/nkpatil/survey
- cd survey
- pip install -r requirements
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

TO create new superuser: python manage.py createsuperuser


Note: login pages are not yet implemented. To test we can simply login into admin panel using below url and credentials.
URL: http://localhost:8000/admin/


Deployed URL: https://demo-surveyform.herokuapp.com/
user: admin
Password: Admin@123!
