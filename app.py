from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/survey')
def home():
    return render_template("survey.html")

@app.route('/', methods=['GET','POST'])
def login():
    error = None
    if (request.method == 'POST'):
        if (request.form['userid'] != '101'):
            error = 'Invalid userID. Please try again.'
        else:
            #return render_template("survey.html")
            return redirect(url_for('home'))
    return render_template('index.html',error=error)

if (__name__ == '__main__'):
    app.run(debug=True)
