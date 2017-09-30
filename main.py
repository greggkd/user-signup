from flask import Flask, request, redirect, render_template
import cgi
import os
import re

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    return render_template('signup.html')

@app.route('/validate_input', methods=['POST'])  
def validate_input():
    name=request.form['username']
    password=request.form['password']
    verify=request.form['verify']
    email=request.form['email']

    name_error=''
    password_error=''
    verify_error=''
    email_error=''

    
    if name == '':
        name_error = 'Pleae enter a valid Name: it can not be left blank.'

    if password == '':
        password_error = 'Please enter a valid Password: it can not be left blank.'
    if password != '' and verify == '':
        verify_error = 'Please verify the password.'
    elif password != verify:
        verify_error = 'The passwords do not match'

    
    if checkforspacesandsize(name):
        name_error = "Username is not allowed to contain spaces and must be 3 to 20 characters long."

    if email != '':
        if checkforspacesandsize(email):
            email_error = "Email can not contain spaces and must be 3 to 20 characters long."
        if not validate_email(email):
            email_error = "Email must contain a \'@\' and a \'.\' and be 3 to 20 characters long, with no spaces."

    if not password_error and not verify_error and not name_error and not email_error:
        return render_template('hello_greeting.html',name=name)
    elif password_error or verify_error or name_error or email_error:
        return render_template('signup.html',name_error=name_error,username=name,
        password_error=password_error,verify_error=verify_error,email=email,
        email_error=email_error)
    
def checkforspacesandsize(text):

    if ' ' in text:
        return True
    elif len(text) < 3 or len(text) > 20:
        return True
    
    return False

def validate_email(text):

    if len(text) > 3 and len(text) < 21:
        if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', text) != None:
            return True
        else:
            return False
    else:
        return False

    
"""
@app.route('/welcome', methods=['POST','GET'])
def welcome():
    name=request.form['username']
    return render_template('hello_greeting.html',name=name)
"""

app.run()