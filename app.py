from sqlite3 import Cursor
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
        pnumb=request.form['phone']
        gender=request.form['gender']

        if len(password)<8:
            return render_template('signup.html',msg='password should be eight characters')
        else:
            sql= 'insert into clientdetails(name,email,password,phone,gender)values(%s,%s,%s,%s,%s)'
            cursor.execute(sql,(name,email,password,pnumb,gender))
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

        sql = 'select * from clientdetails where email =%s and password= %s'   
        cursor.execute(sql,(email,password)) 

        if  cursor.rowcount==0:
            return render_template("login.html", msg="invalid credentials")
        else:
            session['key']=password

            return render_template('home.html')
    else: 
        return render_template('login.html')

@app.route("/")
def index():
    if 'key' in session:
        return render_template('home.html')
    else:
        return redirect('/login')
    
@app.route("/about")
def about():
    if 'key' in session:
        return render_template('about.html')
    else:
        return redirect('/login')
    
@app.route("/services")
def services():
    if 'key' in session:
        conn=pymysql.connect(host='localhost',user='root',password='',database='ean254.com')
        cursor=conn.cursor()
        sql = 'select * from services'
        cursor.execute(sql)
        if cursor.rowcount ==0:
            return render_template('services.html')
        else:
            rows=cursor.fetchall()
            return render_template('services.html', rows=rows)
    else:
        return render_template("/login")    

   
 
@app.route("/contact")
def contact():
    if 'key' in session:
        return render_template('contact.html')
    else:
        return redirect('/login') 
    
@app.route("/logout")
def logout():
    session.pop("key", None)
    return redirect("/login")




if __name__ == '__main__':
    app.run(debug=True)