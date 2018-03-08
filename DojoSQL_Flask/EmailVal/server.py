from flask import Flask, render_template, redirect, url_for, session, request, flash
from mysqlconnection import MySQLConnector
import re #validation
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'the key to the highway'
mysql = MySQLConnector(app, 'mydb')

#mysql = MySQLConnector(app, 'mydb')
#print mysql.query_db("SELECT * FROM EmailVal")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
    email = request.form['email']
    session['email'] = email
    if len(email) < 1:                      #email not entered 
        print "================================="
        flash('Please enter an email address.')
        return redirect('/')
    elif not EMAIL_REGEX.match(email):      #email not valid 
        return redirect('/')
# If we get here the email is validated
    query = "SELECT email_address FROM emails WHERE email_address=:email_to_check"
    data = {'email_to_check':email}
    email_check = mysql.query_db(query, data)
    if (email_check):  #found a match
        return redirect('/success')
    else:              #add new email 
        query = "INSERT INTO emails (email_address, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        data = {'email': email}
        mysql.query_db(query, data) 
        return redirect('/success')

@app.route('/success')
def success():
    query = "SELECT email_address, DATE_FORMAT(created_at, '%M %e, %Y %h:%i%p') AS 'date' FROM emails"
    emails = mysql.query_db(query)
    return render_template('success.html', emailstolist=emails, email=session['email'])

app.run(debug=True)