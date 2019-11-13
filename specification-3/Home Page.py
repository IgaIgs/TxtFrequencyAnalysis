# imports the Flask library and installs the needed libraries
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


# binds a URL to the login function
# specifies the GET and POST methods as by default only GET
# we will need to POST request after logging in
@app.route('/', methods=['GET', 'POST'])
# defines the login function, anything outside will be rendered in the browser
def login():
    # sets error to None
    error = None
    # checks that a user is posting data
    if request.method == 'POST':
        # checks that the username and password are equal to predefined values
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            # displays an error if username and password don't match the given values
            error = 'Invalid login, please try again'
        else:
            # if they match then redirect to the home page
            return redirect(url_for('home'))
    # renders the login.html file
    return render_template("login.html", error=error)


# binds a URL to the home function
@app.route('/home')
# defines the home function, anything outside will be rendered in the browser
def home():
    # renders the homePageHTML.html file
    return render_template("homePageHTML.html")


# binds a URL to the first function
@app.route('/first')
# defines the first function, anything outside will be rendered in the browser
def first():
    # gets the file path for spec1
    text = open('/Users/georgehayfield/PycharmProjects/practical-3/specification-1/char_freq_plot.py', 'r+')
    content = text.read()
    text.close()
    # renders the spec1.html file
    return render_template("spec1.html", text=content)


# binds a URL to the second function
@app.route('/second')
# defines the second function, anything outside will be rendered in the browser
def second():
    # renders the spec2.html file
    return render_template("spec2.html")

# binds a URL to the third function
@app.route('/third')
# defines the second function, anything outside will be rendered in the browser
def third():
    # renders the spec2.html file
    return render_template("spec3.html")

# binds a URL to the fourth function
@app.route('/fourth')
# defines the fourth function, anything outside will be rendered in the browser
def fourth():
    # renders the spec4.html file
    return render_template("spec4.html")


# takes the name of the current module as an argument
if __name__ == '__main__':
    # runs the application of the local development server
    # setting debug to true will give more in depth error report
    app.run(debug=True)
