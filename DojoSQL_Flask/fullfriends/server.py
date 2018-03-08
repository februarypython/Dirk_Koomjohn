from flask import Flask, render_template, redirect, request, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'fullfriends')
#print mysql.query_db("SELECT * FROM fullfriends")
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        print "=================  G E T  ===================="
        query = "select name, age, since from fullfriends"
#        query = "SELECT CONCAT_WS(' ', first_name, last_name) AS 'name', age, DATE_FORMAT(created_at, '%M %D') AS 'since', DATE_FORMAT(created_at, '%Y') as 'year' FROM friends"
        friends = mysql.query_db(query)
        return render_template('index.html', dbfriends=friends)
    else:  
        print "================== improper method ===================="

@app.route('/addfriends', methods=['POST'])
def addfriends():
    if request.method == 'POST':
        print "==================  P O S T  ===================="
        query = "INSERT INTO fullfriends VALUES (null, :name, now(), :age, NOW(), NOW())"
        data = {
            'name': request.form['name'],
            'age': request.form['age'],
        }
        mysql.query_db(query, data)
        return redirect('/')
    else: 
        print "================= improper method (add) ================="
#        flash "improper method"

app.run(debug=True)