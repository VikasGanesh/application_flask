from flask import Flask,render_template,request,flash,redirect,url_for
import flask
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from datetime import timedelta
from Databaseaccess import Databaseaccess as DBA

app=Flask(__name__)
app.secret_key = 'super secret key'


login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
    print "in load_user"
    print userid
    return User(userid,"","")



@app.before_request
def before_request():
    flask.session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=60)
    flask.session.modified = True
    flask.g.user = current_user



class User(UserMixin):
    def __init__(self,id,name,password):
        self.id = id
        self.name = name
        self.password = "password"
    def __repr__(self):
        return "%d/%s/%s" % (self.id,self.name, self.password)
    
    

@app.route('/')
def Home():
    return render_template( 'login.html' )

@app.route('/login', methods = ['POST'])
def Login():
    email=request.form['username']
    password=request.form['password']
    email=str(email)
    password=str(password)
    userslist=DBA.findUserwithemail(email)
    userfound=0
    print userslist
    for users in userslist:
        if users[1]==email:
            userfound=1
            if users[2]==password:
                user=User(int(users[0]),email,password)
                login_user(user)
                return render_template('home.html',user = current_user.name)
            else:
                flash("False",'msg')
                
                
    if userfound==0:
        flash("False",'msg')
        return render_template('login.html')


@app.route('/signup', methods = ['POST'])
def signup():
    try:
        email=request.form['username']
        password=request.form['password']
        email=str(email)
        password=str(password)
        print email,password
        DBA.AddUser(email,password)
        return render_template('login.html')

    except Exception as e:
        print e
                
 

@app.route('/logout', methods = ['POST'] )
def logout():
    try:
        logout_user()
        return redirect(url_for('Home'))
    except Exception as e:
        print e




if __name__ == '__main__':
    app.run()