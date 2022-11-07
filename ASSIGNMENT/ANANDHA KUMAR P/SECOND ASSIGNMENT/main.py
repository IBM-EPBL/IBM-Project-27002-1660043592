from flask import Flask, render_template
import ibm_db

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=2f3279a5-73d1-4859-88f0-a6c3e6b4b907.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=30756;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=gbq63433;PWD=C2hvtayMDEmef0uI",'','')

app=Flask(__name__)

@app.route('/')

def login():
    return render_template('login.html')

@app.route('/register')

def register():
    return render_template('register.html')

@app.route('/home')

def home():
    return render_template('home.html')

if __name__=='__main__':
    app.run(debug = True)