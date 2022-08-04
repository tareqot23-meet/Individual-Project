from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase



config={
    
  "apiKey": "AIzaSyARnQ4UTmCiI9lxzZ5e_xhl6_GbBWdSFRA",
  "authDomain": "personal-projetc-y2-cs.firebaseapp.com",
  "databaseURL": "https://personal-projetc-y2-cs-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "personal-projetc-y2-cs",
  "storageBucket": "personal-projetc-y2-cs.appspot.com",
  "messagingSenderId": "568400764874",
  "appId": "1:568400764874:web:39fcf6679ad0ee46833933",
  "measurementId": "G-ZDTRCJ4CG7"

}



firebase=pyrebase.initialize_app(config)
auth=firebase.auth()
db = firebase.database()
app=Flask(__name__)




app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return render_template('index.html')
        except:
           error = "Authentication failed"
           return error
        return render_template("signin.html")
    else:
        return render_template("signin.html")


    

@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')



@app.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':



        email = request.form['email']
        password = request.form['password']
        bio = request.form['bio']
        fullname = request.form['fullname']
        username = request.form['username']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            user = {"fullname":fullname,"bio":bio,"password":password,"username":username,"email":email}
            db.child("users").child(login_session['user']['localId'] ).set(user)




            return render_template('index.html')

        except:
           error = "Authentication failed"
           return error

 
    else:
         
            return render_template("signup.html")

    







if __name__ == '__main__':
    app.run(debug=True)





    