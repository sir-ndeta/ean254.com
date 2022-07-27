from crypt import methods
from flask import *

import pymysql
app = Flask(__name__)

app.secret_key = 'e3#A7@N_3yhpargotohp'

@app.route('/signup',methods=['GET','POST'])
def signup():
    conn=pymysql.connect(host='localhost',user='root',password='',database='ean254.com')
    cursor=conn.cursor()

    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        phone=request.form['phone']
        gender=request.form['gender']

        if len(password)<8:
            return render_template('form1.html',msg='password should be eight characters')
        else:
            sql= 'insert into user(names,email,password,phone,gender)values(%s,%s,%s,%s,%s)'
            cursor.execute(sql,(name,email,password,phone,gender))
            conn.commit()
            return render_template('login.html',msg='saved succesfuly')
    else:
        return render_template('signup.html')


@app.route('/login', methods=["GET","POST"])
def login():
    conn = pymysql.connect(host='localhost', user='root', password="", database="ean254.com")
    cursor = conn.cursor() 

    if request.method =="POST":
        email=request.form["email"]
        password=request.form["password"]

        sql = 'select * from user where email =%s and password= %s'   
        cursor.execute(sql(email,password)) 

        if  cursor.rowcount==0:
            return render_template("login.html", msg="invalid credentials")
        else:
            session['key']=email

            return render_template('index.html')
    else: 
        return render_template('login.html')

@app.route("/")
def index():
    if 'key' in session:
        return render_template('home.html')
    else:
        return redirect('/login')

