from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, RadioField,BooleanField
from wtforms.validators import DataRequired, Email
import bleach
import re

app = Flask(__name__)

def sanitize_input(input_str):
    return input_str.strip()

def validate_email(email):
    email_regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(email_regex, email)



def sanitize_input(input_data):
    allowed_tags = ['b', 'i', 'u', 'em', 'strong', 'a']
    return bleach.clean(input_data, tags=allowed_tags, strip=True)


@app.route('/', methods=['GET' , 'POST'] )
def forms():
    return render_template('forms.html')

@app.route('/data', methods=['POST', "GET"])
def data():
    if request.method == 'POST':
        data = request.form
        firstName = sanitize_input(request.form.get('first_name'))
        lastName = sanitize_input(request.form.get('last_name'))
        email = sanitize_input(request.form.get('email'))
        country = request.form.get('country')
        message =sanitize_input(request.form.get('msg'))
        gender_choice = request.form.get('gender-choice')
        reparation_check = request.form.get('reparationcheck')
        commande_check = request.form.get('commandecheck')
        autre_check = request.form.get('Autrecheck')
        print(firstName,lastName,email,country)
        
        response = (
                f"Thank you for reaching us.<br>"
                f"First Name: {firstName}<br>"
                f"Last Name: {lastName}<br>"
                f"Email: {email}<br>"
                f"Country: {country}<br>"
                f"Message: {message}<br>"
                f"Gender: {gender_choice}<br>"
                f"Reparation: {reparation_check}<br>"
                f"Command: {commande_check}<br>"
                f"Other: {autre_check}"
            )

        return response
    else:
        return redirect(url_for('forms'))

if __name__ == "__main__":
    app.run(debug=True)

 