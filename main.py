from flask import Flask,render_template,request,flash,redirect,url_for
import flask
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from datetime import timedelta
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
    username=request.form['username']
    password=request.form['password']
    print username,password
    username=str(username)
    password=str(password)
    user=""
    if username=="admin":
        if password=="admin":
            user=User(2,username,password)
            print user
            login_user(user)
            return render_template('home.html',user = current_user.name,)
        else:
            flash("False",'msg')
            return render_template('login.html')
    else:
        flash("False",'msg')
        return render_template('login.html')

@app.route('/logout', methods = ['POST'] )
def logout():
    try:
        logout_user()
        return redirect(url_for('Home'))
    except Exception as e:
        print e




if __name__ == '__main__':
    app.run()