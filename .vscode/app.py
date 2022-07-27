from flask import *
import pymysql

app = Flask(__name__)

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

