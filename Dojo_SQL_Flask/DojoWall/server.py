from flask import Flask, render_template, redirect, url_for, session, request, flash
from mysqlconnection import MySQLConnector
import re                               #validation
import md5                              #imports md5 hashing module 
import os, binascii                     #import salt 
salt = binascii.b2a_hex(os.urandom(15)) #create the salt string
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#NAME_REGEX = re.compile(r'[\sa-zA-Z.-]{2,}$') #regex to control allowed and number of (2) characters
#PW_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$') #regex for password, confirm 1 uppercase, 1 num
app = Flask(__name__)
mysql = MySQLConnector(app, 'walldb')
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
        err-flash = true
    if len(l_name) < 2: 
        flash('Please enter a last name.')
        err-flash = true
    if len(p_word) < 8:                
        flash('Password must be at least 8 characters.')
        err-flash = true
    if p_word != p_word_conf:            # password confirmation
        flash('Password confirmation invalid.')
        err-flash = true
    if len(email) < 7:                    # incomplete email 
        flash('Please enter a full email address.')
        err-flash = true
    if not EMAIL_REGEX.match(email):      # email not valid 
        err-flash = true

# something didn't pass mustar
    if err-flash:
        return render_template('index.html')   
#        return render_template('index.html', first_name=first_name, last_name=last_name, email=email)   
    else: 
# raw data ok / check for email match
        query = "SELECT * FROM users WHERE email=:email_to_check"
        data = {'email_to_check':email}
        email_check = mysql.query_db(query, data)
        if (email_check):  #found a match so don't add / check password
            print "==================== email already exists =========================="

            return redirect('/thewall')


    else:              #add new email/user 
        print "==================insert=================="   #list of dictionary pairs for sqlalchemy
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
        data = {'first_name': f_name, 'last_name': l_name, 'email': email, 'password': p_word}
        mysql.query_db(query, data)
        current_id = user.id
        session['user_id'] = mysql.query_db(users_query, users_data)
        return redirect('/thewall')


 #       hashed_password = md5.new(password + salt).hexdigest() #encrypt password
 #       #add the user
 #       users_query = "INSERT INTO users VALUES (null, :first_name, :last_name, :email, :password, NOW(), NOW(), :salt)"
 #       users_data = {
 #           'first_name': first_name,
 #           'last_name': last_name,
 #           'email': email,
 #           'password': hashed_password,
 #           'salt': salt
 #       }




    email = request.form['email']
    password = request.form['password']
    #query to find user
    query = "SELECT id, first_name, email, password, salt FROM users WHERE email=:email_entered LIMIT 1"
    data = {
        'email_entered': email
    }
    user_found = mysql.query_db(query, data)

@app.route('/message', methods=['POST'])
def message():
    #if user not in session, redirect
    if 'user_id' not in session:
        return redirect('/')
    else:
        post_query = "INSERT INTO messages VALUES (NULL, :id, :post, NOW(), NOW())"
        post_data = {
            'id': session['user_id'],
            'post': request.form['post']
        }
        mysql.query_db(post_query, post_data)
        return redirect('/wall')

@app.route('/comment', methods=['POST'])
def comment():
    #if user not in session, redirect
    if 'user_id' not in session:
        return redirect('/')
    else:
        comment_query = "INSERT INTO comments VALUES (NULL, :userid, :msgid, :post, NOW(), NOW())"
        comment_data = {
            'userid': session['user_id'],
            'msgid': request.form['msgid'],
            'post': request.form['comment']
        }
        mysql.query_db(comment_query, comment_data)
        return redirect('/wall')
        
@app.route('/thewall')
def thewall():
 #if user not in session, redirect
    if 'user_id' not in session:
        return redirect('/')
    else: #user logged in, personalize page
        user_query = "SELECT first_name FROM users WHERE id=:logged_id"
        user_data = {'logged_id': session['user_id']}
        user=mysql.query_db(user_query, user_data)

        #query posts(aka messages)
        post_query = "SELECT CONCAT_WS(' ', first_name, last_name) AS 'poster', messages.user_id AS 'poster_id', message AS 'post', DATE_FORMAT(messages.created_at, '%M %e, %Y') AS 'posted', messages.id AS 'msgid', messages.created_at FROM users JOIN messages ON messages.user_id=users.id ORDER BY DATE_FORMAT(messages.created_at, '%M %e, %Y') DESC"
        posts = mysql.query_db(post_query)
        #loop through each post and query for any comments
        comment_query = "SELECT CONCAT_WS(' ', first_name, last_name) AS 'commenter', comment, DATE_FORMAT(comments.created_at, '%M %e, %Y') AS 'commented', message_id from comments JOIN users on users.id=comments.user_id ORDER BY DATE_FORMAT(comments.created_at, '%M %e, %Y')"
        comments = mysql.query_db(comment_query)

        now = datetime.now()
        return render_template('wall.html', user=session['first_name'], posts=posts, comments=comments, now=now)

@app.route('/signout')
def signout():
    session.pop('user_id', 'first_name')
    return redirect('/')

app.run(debug=True)