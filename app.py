from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps

app = Flask(__name__)

app.secret_key = "random"

# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

@app.route('/')
@login_required
def home():
    return render_template("index.html")

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if (request.method == 'POST'):
        if (request.form['userid'] != '101'):
            error = 'Invalid userID. Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('home'))

    return render_template('login.html',error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if (__name__ == '__main__'):
    app.run(debug=True)