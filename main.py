from flask import Flask,render_template,request,flash
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user

app=Flask(__name__)

class User(UserMixin):
    def __init__(self,name,password):
        self.name = name
        self.password = password
    def __repr__(self):
        return "%s/%s" % (self.name, self.password)


@app.route('/')
def Home():
    return render_template( 'login.html' )

@app.route('/login', methods = ['POST'])
def Login():
    username=request.form['username']
    password=request.form['password']
    user=""
    if username=="admim":
        if password=="admin":
            user=User(str(username),str(password))
            login_user(user)
        else:
            flash('msg',"False")
            return render_template('login.html')
    else:
        flash('msg',"False")
        return render_template('login.html')






if __name__ == '__main__':
    app.run()