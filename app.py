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
        pnumb=request.form['pnumb']
        gender=request.form['gender']

        if len(password)<8:
            return render_template('signup.html',msg='password should be eight characters')
        else:
            sql= 'insert into clientdetails(name,email,password,pnumb,gender)values(%s,%s,%s,%s,%s)'
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
    
@app.route('/adminlogin', methods=["GET","POST"])
def adminlogin():
    conn = pymysql.connect(host='localhost', user='root', password="", database="ean254.com")
    cursor = conn.cursor() 

    if request.method =="POST":
        email=request.form["email"]
        password=request.form["password"]

        sql = 'select * from admin where email =%s and password= %s'   
        cursor.execute(sql,(email,password)) 

        if  cursor.rowcount==0:
            return render_template("adminlogin.html", msg="invalid credentials")
        else:
            session['key']=password

            return render_template('admin.html')
    else: 
        return render_template('adminlogin.html')

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
    
@app.route('/assignments')
def assignments():
    conn=pymysql.connect(host='localhost',user='root',password='',database='ean254.com')
    cursor=conn.cursor()

    sql='select*from assignments'
    cursor.execute(sql)

    if cursor.rowcount==0:
        return render_template('assignment.html',msg='No assignment available')
    else:
        rows=cursor.fetchall()
        return render_template('assignment.html',rows=rows)

   
 
@app.route("/contact")
def contact():
    if 'key' in session:
        return render_template('contact.html')
    else:
        return redirect('/login') 
    
@app.route("/admin")
def admin():
    if 'key' in session:
        return render_template('admin.html')
    else:
        return redirect('/login') 
    
@app.route("/assignment")
def assignment():
    if 'key' in session:
        return render_template('assignment.html')
    else:
        return redirect('/login') 
    
@app.route("/logout")
def logout():
    session.pop("key", None)
    return redirect("/login")

import requests
import datetime
import base64
from requests.auth import HTTPBasicAuth
@app.route('/mpesa', methods = ['POST','GET'])
def mpesa():
        if request.method == 'POST':
            phone = str(request.form['phone'])
            amount = str(request.form['amount'])
            # GENERATING THE ACCESS TOKEN
            consumer_key = "GTWADFxIpUfDoNikNGqq1C3023evM6UH"
            consumer_secret = "amFbAoUByPV2rM5A"

            api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials" #AUTH URL
            r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

            data = r.json()
            access_token = "Bearer" + ' ' + data['access_token']

            #  GETTING THE PASSWORD
            timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
            passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
            business_short_code = "174379"
            data = business_short_code + passkey + timestamp
            encoded = base64.b64encode(data.encode())
            password = encoded.decode('utf-8')


            # BODY OR PAYLOAD
            payload = {
                "BusinessShortCode": "174379",
                "Password": "{}".format(password),
                "Timestamp": "{}".format(timestamp),
                "TransactionType": "CustomerPayBillOnline",
                "Amount": amount,  # use 1 when testing
                "PartyA": phone,  # change to your number
                "PartyB": "174379",
                "PhoneNumber": phone,
                "CallBackURL": "https://modcom.co.ke/job/confirmation.php",
                "AccountReference": "account",
                "TransactionDesc": "account"
            }

            # POPULAING THE HTTP HEADER
            headers = {
                "Authorization": access_token,
                "Content-Type": "application/json"
            }

            url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest" #C2B URL

            response = requests.post(url, json=payload, headers=headers)
            print (response.text)
            return("Please complete your payment on the phone")
        else:
            return render_template('services.html')


@app.route('/single/<SN>')
def single(SN):
    conn=pymysql.connect(host='localhost',user='root',password='',database='ean254.com')
    cursor=conn.cursor()

<<<<<<< HEAD
    sql='select*from services where SN=%s' 
=======
    sql='select*from services where SN.=%s' 
>>>>>>> 282d23515a621f0da42a3504dbe60829282f5a27
    cursor.execute(sql,(SN))
    row=cursor.fetchone
    return render_template('single.hml',row=row)

<<<<<<< HEAD
@app.route('/save',methods=['GET','POST'])
def book():
    conn=pymysql.connect(host='localhost',user='root',password='',database='ean254.com')
    cursor=conn.cursor()

    if request.method=='POST':
        ClientName=request.form['ClientName']
        ClientPhoneNumber=request.form['ClientPhoneNumber']
        Location=request.form['Location']
        Service=request.form['Service']
        

        sql='insert into assignments(ClientName,ClientPhoneNumber,Location,Service)values(%s,%s,%s,%s)'
        cursor.execute(sql,(ClientName,ClientPhoneNumber,Location,Service,))
        conn.commit()
        return render_template('save.html',msg='Booking reserved')

    else:
        return render_template('login.html')

=======
>>>>>>> 282d23515a621f0da42a3504dbe60829282f5a27



if __name__ == '__main__':
    app.run(debug=True)