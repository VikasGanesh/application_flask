from flask import Flask,render_template,request
app=Flask(__name__)


@app.route('/')
def Home():
    return render_template( 'login.html' )

@app.route('/login', methods = ['POST'])
def Login():
    username=request.form['username']
    password=request.form['password']
    





if __name__ == '__main__':
    app.run()