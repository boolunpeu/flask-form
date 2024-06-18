# Feedback Form Creation
The form collects the following information:

First Name (required)
Last Name
Email (required)
Country (dropdown)
Problem Description
Gender (radio buttons)
Types of Issues (checkboxes for Reparation, Command, and Other)

![form-noerror](https://github.com/boolunpeu/flask-form/assets/131985567/c2c04551-f99f-438e-ba50-75bcabeba6e4)


2. Form Validation Error
When the user attempts to submit the form without filling in required fields (like "First Name"), an error message prompts the user to fill out the missing field(s).

![form-error](https://github.com/boolunpeu/flask-form/assets/131985567/7abd03b3-a41d-4b3e-9a0e-71ccf0cf5af6)


3. Successful Form Submission
Once the user fills out all the required fields and submits the form, the entered data is displayed on a new page, confirming successful submission.

![feedback + data](https://github.com/boolunpeu/flask-form/assets/131985567/5dea2361-92d7-4cc0-bdd1-39a1d7466f8d)


4. Data Display on Submission
The submitted data is displayed as follows:

First Name: TEST
Last Name: Test
Email: test@test.com
Country: Belgium
Message: Test
Gender: Other
Reparation: 1
Command: 2
Other: 3

![Submitted Data](attachment:/mnt/data/feedback + data.PNG)

5. Input Sanitization for Security
To protect against cross-site scripting (XSS) attacks, the project includes input sanitization. This ensures that any script tags or malicious code are removed from user inputs, maintaining the security and integrity of the data.

![no xss](https://github.com/boolunpeu/flask-form/assets/131985567/f2a2ca26-607c-416c-83d8-241903abdd64)

