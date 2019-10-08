# Dynamic-PyStroke
Behavioural Biometrics based on Keystroke Dynamics

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
1. As a user, I want to log into the website without worrying about someone else seeing and using my password.  (Estimated Time - 50 days) (Priority 9.5)
2. As a user, I want the software to study my typing pattern when I register on the website.  (Estimated Time - 12 days) (Priority 10)
3. As a user, I want my typing pattern data to be secured.  (Estimated Time - 2 days) (Priority 6)
4. As a user, I want to be able to use a secondary authentication to login to the website if I am unable to match the typing pattern. (Estimated Time - 2 days) (Priority 7)
5. As a user, I want to see the secondary authentication showing just a set of images that I choose from. (Estimated Time - 4 days) (Priority 7)
6. As a user, I want to choose the number of images and the sequence of images as a secondary authentication. (Estimated Time - 8 days) (Priority 7)
7. As a user, I want to receive an email when my credentials are used to log into the website but the typing pattern doesn't match my typing patter.  (Estimated Time - 9 days) (Priority 2)
8. As a user, I want to be able to reset my password if and when I forget by getting a code in my email.  (Estimated Time - 3 days) (Priority 5)

## PART B

### Tasks
1. Website - Create the website (Estimated Duration - 12 days) (Priority 9.5): Ben Minikwu
2. Key Listener - Create Key Listener to collect keystroke timings  (Estimated Duration - 10 days) (Priority 10): Surya Kakria
  2.1 Database - Store collected timings (Estimated Duration - 5 days) (Priority 9.5): Armin Abazari
  2.2 Machine Learning - Create Machine learning algorithms to study the timings (Estimated Duration - 24 days) (Priority 8.5): Affad Shaikh, Surya Kakria, Shervon Thomas, Armin Abazari, Ben Minikwu
3. Encryption - Encrypt the database that contains the timings  (Estimated Duration - 5 days) (Priority 6): Armin Abazari
4+5.  Secondary Authentication part 1 - Create a page that has a series of images.  (Estimated Duration - 3 days) (Priority 7): Shervon Thomas
6. Secondary Authentication part 2 - Allow a user to choose a number of images in a specific order and compare them to the existing pattern.  (Estimated Duration 12 days) (Priority 7): Shervon Thomas, Surya Kakria
7. Notification - Create a program that sends a user an email when the primary authentication fails to recognize the pattern. (Estimated Duration - 8 days) (Priority 2): Affad Shaikh
8. Password Retrieval - Create a program to send a randomly generated code to a users email and allow the user to reset the password when the code entered matches the randomly generated code sent via email.  (Estimated Duration - 6 days) (Priority 5): Ben Minikwu, Affad Shaikh

### Milestone 1
1. Website - 12 days
2. Key Listener - 10 days
2.1 Database - 5 days
4+5 Secondary Authentication part 1 - 3 days

### 2 Iterations for Milestone 1
Iteration 1 (2 Weeks):
  Create the website
  Secondary Authentication Part 1

Iteration 2 (2 Weeks):
  Key Listener
  Database

### Velocity
Timeline: 4 Weeks to Milestone 1, 5 Weeks to Milestone 2
Starting Velocity: 40%
  Total: 10 hours per week
  Current: 4 hours per week
