COMMANDS:
------------
run django server -> py manage.py runserver (for this you have to be in the same dir where the manage.py file is placed)



REQUIREMENTS:
-------------
asgiref==3.4.1
Django==3.2.9
psycopg2==2.9.1
pytz==2021.3
sqlparse==0.4.2

*The project also contains a requirements.txt file*



INSTALLATIONS:
---------------
to create a django virtual-env ->  py -m venv denv
to activate 'denv' -> (in command line) denv\Scripts\activete
to deactivate 'denv' -> (again in cmd) deactivate
to install django -> (cmd) pip install django


TECHSTACK
---------------
* HTML5 
* CSS3
* JavaScript
* Django


DEPLOYMENT DETAILS
-------------------
The web application is deployed on 'pythonanywhere.com' which has a good support for python based applications



FUNCTIONALITIES ACHIEVED
--------------------------
* MCQ pattern assessment
* Question Pool
* Questions only from pool
* Number of questions in the pool is greater than the number of questions displayed
* Timer for whole question
* Questions are shuffled everytime time quiz appears
* Assessment Score is generated at the end, also the correct, wrong and unanswered questions are shown  along with their answers



SOME FEATURES
--------------------------
* Login and register to keep record of tests taken
* Simple User Interface for a '"gradual learning curve"'
* Theme across all pages



ADMIN FUNCTIONALITIES
--------------------------
* Admins can:-
    - create test
    - add questions in the pool
    - set number of question appear in test
    - set duration of test
    - Preview the page of all submitted test results.


*This Django web application is designed, developed and deployed by Anurag Banerjee*