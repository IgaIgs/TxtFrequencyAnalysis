from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid login, please try again'
        else:
            return redirect(url_for('home'))
    return render_template("login.html", error=error)


@app.route('/home')
def home():
    return render_template("homePageHTML.html")


@app.route('/first')
def first():
    return render_template("spec1.html")


@app.route('/second')
def second():
    return render_template("spec2.html")


@app.route('/fourth')
def fourth():
    return render_template("spec4.html")


if __name__ == '__main__':
    app.run(debug=True)
