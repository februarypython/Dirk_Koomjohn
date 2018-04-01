from flask import Flask, render_template, redirect, url_for, session, request, flash
from mysqlconnection import MySQLConnector
import re #validation
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app, 'lognregdb')
app.secret_key = 'the key to the highway'

#print mysql.query_db("select * from users")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lognreg', methods=['POST'])
def validate():
    f_name = request.form['first_name']
    l_name = request.form['last_name']
    p_word = request.form['password']
    p_word_conf = request.form['password_conf']
    email = request.form['email']

# *** v a l i d a t i o ns ******
    if len(f_name) < 2:                 # must be at least 2 chars 
        flash('Please enter a first name.')
        return redirect('/')
    if len(l_name) < 2:                  # must be at least 2 chars 
        flash('Please enter a last name.')
        return redirect('/')
    if len(p_word) < 8:                
        flash('Password must be at least 8 characters.')
        return redirect('/')
    if p_word != p_word_conf:            # password confirmation
        flash('Password confirmation invalid.')
        return redirect('/')
    if len(email) < 7:                      # incomplete email 
        flash('Please enter a full email address.')
        return redirect('/')
    elif not EMAIL_REGEX.match(email):      # email not valid 
        return redirect('/')

# If we get here the all input is validated
    query = "SELECT * FROM users WHERE email=:email_to_check"
    data = {'email_to_check':email}
    email_check = mysql.query_db(query, data)
    if (email_check):  #found a match so don't add
        print "==================== email already exists =========================="
        return redirect('/success')
    else:              #add new email 
        print "==================insert=================="
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
        data = {'first_name': f_name, 'last_name': l_name, 'email': email, 'password': p_word}
        mysql.query_db(query, data) 
        return redirect('/success')

@app.route('/success')
def success():
 #  query = "SELECT email_address, DATE_FORMAT(created_at, '%M %e, %Y %h:%i%p') AS 'date' FROM emails"
 #  emails = mysql.query_db(query)
 #  return render_template('success.html', emailstolist=emails, email=session['email'])
    return render_template('success.html')

app.run(debug=True)