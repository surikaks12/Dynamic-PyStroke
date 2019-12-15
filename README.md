# Dynamic-PyStroke
Behavioural Biometrics based on Keystroke Dynamics

## How to run the application:

### Environment to run the application:
- Python 3.7.8
- Pip 18.1
- Virtual Environment 16.0.0

### Run Application command:
- from application root activate the virtual environment

#### Mac OS
source ./venv/bin/activate
#### Windows OS
execute/run "activate" file

### Run Application command

cd into Dynamic-PyStroke_NotWorking/django/myprojects

Run command python manage.py runserver

Copy and paste into web browser: http://127.0.0.1:8000/dynamicpystroke/

Once you have launched the website, click demo to go to the login page

To see the downloaded file, type in the password and hit the enter key. Hitting the submit button will not download the file.

### Test:
- To test the extractor:
 cd into the extractor folder then run command pytest -v test_extractor.py

Unable to run tests for django due to lack of connectivity to the database.

### Coverage:
- How to run test coverage After virutal environment activation, from inside the extractor folder, Run "pytest --cov=helper test_extractor.py"
- To view the HTML representation of the coverage cd into extractor/htmlcov and open helper_py.html

## Install FAQ
- Django not found/ installed
Some user reported that in the first run Django was not loaded from Virtual Environment. In such case please install Django after virtual environment activation by

pip install Django

- plugin/ module not found (ModuleNotFoundError)
Due to the conflict related to python version some plugin might not load properly from virtual enviroment. To fix such issue, install the plugin required by project which is listed in file "requrement.txt" located in repository. Single command installer is as following.

pip install -r ./Requirements.txt

## PART A

### Team Members:
  Surya Kakria,
  Shervon Thomas,
  Ben Minikwu,
  Armin Abazari,
  Affad Shaikh

### Stakeholders:
- All end users.
- All developers that incorporate our authentication software.
- Business institutions that implement the authentication software.
- Members of Dynamic PyStroke.
- Professor of Software Development at CGU for Fall 2019 Semester.

### User Stories:
1. Website: As a user, I want to log into the website without worrying about someone else seeing and using my password.  (Estimated Time - 10 days) (Priority 10)
2. Keystroke Dynamics: As a user, I want the software to study my typing pattern when I register on the website.  (Estimated Time - 20 days) (Priority 10)
3. Encryption: As a user, I want my typing pattern data to be secured. (Estimated Time - 2 days) (Priority 20)
4. Authentication Phase 1: As a user, I want to be able to use a secondary authentication to login to the website if I am unable to match the typing pattern. (Estimated Time - 2 days) (Priority 30)
5. Authentication Phase 2: As a user, I want to see the secondary authentication showing just a set of images that I choose from. (Estimated Time - 4 days) (Priority 30)
6. Authentication Phase 3: As a user, I want to choose the number of images and the sequence of images as a secondary authentication. (Estimated Time - 3 days) (Priority 30)
7. Notification: As a user, I want to receive an email when my credentials are used to log into the website but the typing pattern doesn't match my typing patter.  (Estimated Time - 5 days) (Priority 50)
8. Password Retrieval: As a user, I want to be able to reset my password if and when I forget by getting a code in my email.  (Estimated Time - 3 days) (Priority 40)

## PART B

### Tasks
1. Website:
- Create the website (Estimated Duration - 7 days) (Priority 10): Ben Minikwu
- Local Host - The website to be hosted locally (Estimated Duration - 1 days) (Priority 10 ): Ben Minikwu
- Registration - A user can register in the Website (Estimated Duration - 1 days) (Priority 20): Ben Minikwu
- Log in - A user Log into the website (Estimated Duration - 1 days) (Priority 20): Ben Minikwu

2. Keystroke Dynamics:
- Key Listener - Create Key Listener to collect keystroke timings  (Estimated Duration - 5 days) (Priority 10): Surya Kakria
- Database - Store collected timings (Estimated Duration - 5 days) (Priority 5): Armin Abazari
- Machine Learning - Create Machine learning algorithms to study the timings (Estimated Duration - 10 days) (Priority 20): Affad Shaikh, Surya Kakria, Shervon Thomas, Armin Abazari, Ben Minikwu

3. Encryption: Encrypt the database that contains the timings  (Estimated Duration - 2 days) (Priority 30): Armin Abazari

4. Authentication Phase 1: Create a page that has a series of images.  (Estimated Duration - 3 days) (Priority 30): Shervon Thomas

5. Authentication Phase 2: Allow a user to choose a number of images in a specific order and compare them to the existing pattern. (Estimated Duration 4 days) (Priority 30): Shervon Thomas, Surya Kakria

6. Authentication Phase 3: Authentication registration (Estimated Duration 3 days) (Priority 30): Shervon Thomas

7. Notification: Create a program that sends a user an email when the primary authentication fails to recognize the pattern. (Estimated Duration - 5 days) (Priority 50): Affad Shaikh

8. Password Retrieval: Create a program to send a randomly generated code to a users email and allow the user to reset the password when the code entered matches the randomly generated code sent via email.  (Estimated Duration - 3 days) (Priority 40): Ben Minikwu, Affad Shaikh

### Milestone 1
1. Website - 10 days
2. Key Listener - 5 days
3. Database - 5 days

### 2 Iterations for Milestone 1
Iteration 1 (2 Weeks):
- Create the website

Iteration 2 (2 Weeks):
- Key Listener
- Database

### Milestone 2
1. Extracting Data
2. Machine Learning
3. Secondary Authentication

### Velocity
- Timeline: 4 Weeks to Milestone 1, 5 Weeks to Milestone 2
- Starting Velocity: 45%
- Total: 40 hours per week
- Current: 18 hours per week

### Burndown Chart
  Uploaded file in Repository called "DPBurndown_ChartM2.png"

  The Burndown Chart is a representation of Milestone 2.

note: Uploaded file in Repository called "DP_Burndown_M1.xlsx" contains burndown chart for Milestone 1.

### Meeting Minutes
Uploaded file in Repository called "PD Meeting Minutes.docx"

### Lessons Learned:
- How to incorporate time management and teamwork into software development.
- Using github to synchronize work on the coding aspect of the project.
- How to work around problems or fix them within a project timeframe.
