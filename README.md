# Feedback Form Creation
The form collects the following information:

First Name (required)
Last Name
Email (required)
Country (dropdown)
Problem Description
Gender (radio buttons)
Types of Issues (checkboxes for Reparation, Command, and Other)

![form-noerror](https://github.com/boolunpeu/flask-form/assets/131985567/c5e950e6-6c4f-454c-897f-ae1891dc9b1c)

2. Form Validation Error
When the user attempts to submit the form without filling in required fields (like "First Name"), an error message prompts the user to fill out the missing field(s).

![form-error](https://github.com/boolunpeu/flask-form/assets/131985567/85f60cf8-2870-40b7-a71b-66aed28bdcf0)

3. Successful Form Submission
Once the user fills out all the required fields and submits the form, the entered data is displayed on a new page, confirming successful submission.

![feedback + data](https://github.com/boolunpeu/flask-form/assets/131985567/d148485b-c81b-4f23-8331-6a1d57ac866e)

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

5. Input Sanitization for Security
To protect against cross-site scripting (XSS) attacks, the project includes input sanitization. This ensures that any script tags or malicious code are removed from user inputs, maintaining the security and integrity of the data.

![test xss](https://github.com/boolunpeu/flask-form/assets/131985567/cac724b6-ace3-4779-b83a-576a9360f538)

![no xss](https://github.com/boolunpeu/flask-form/assets/131985567/d9001da6-a6b7-4c64-a0d0-18538d0737c9)
