from flask import Flask, render_template, request
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)

@app.route('/form')
def form():
    return render_template('wizard.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        weight = request.form['weight']
        height = request.form['height']
        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO info_table VALUES(%s,%s,%s,%s)''',(name,age,weight,height))
        mysql.connection.commit()
        cursor.close()
        return f"Analysing"


    


    




app.run(host = 'localhost', port =5000)
