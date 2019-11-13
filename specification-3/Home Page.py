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
    # gets the file path for book analysis and will allow me to display it
    text = open('/Users/georgehayfield/PycharmProjects/practical-3/specification-1/book_analysis.py', 'r+')
    # gets the file path for char freq and will allow me to display it
    text1 = open('/Users/georgehayfield/PycharmProjects/practical-3/specification-1/char_freq_plot.py', 'r+')
    # gets the file path for the csv writer and will allow me to display it
    text2 = open('/Users/georgehayfield/PycharmProjects/practical-3/specification-1/csvwriter.py', 'r+')
    # gets the file path for the freq and will allow me to display it
    text3 = open('/Users/georgehayfield/PycharmProjects/practical-3/specification-1/freq.py', 'r+')
    # sets a variable content to text
    content = text.read()
    content1 = text1.read()
    content2 = text2.read()
    content3 = text3.read()
    # closes the file reading
    text.close()
    # renders the spec1.html file and passes the text variable to the spec1 html file
    return render_template("spec1.html", text=content, text1=content1, text2=content2, text3=content3)


# binds a URL to the second function
@app.route('/second')
# defines the second function, anything outside will be rendered in the browser
def second():
    # gets the file path for image manipulation and will allow me to display it
    text = open('/Users/georgehayfield/PycharmProjects/practical-3/specification-2/image_manipulation.py', 'r+')
    # sets a variable content to text
    content = text.read()
    # renders the spec2.html file
    return render_template("spec2.html", text=content)

# binds a URL to the third function
@app.route('/third')
# defines the second function, anything outside will be rendered in the browser
def third():
    # gets the file path for the home page central python file and will allow me to display it
    text = open('/Users/georgehayfield/PycharmProjects/practical-3/specification-3/Home Page.py', 'r+')
    # gets the file path for the login html file and will allow me to display it
    text1 = open('/Users/georgehayfield/PycharmProjects/practical-3/specification-3/templates/login.html', 'r+')
    # gets the file path for the homePage html file and will allow me to display it
    text2 = open('/Users/georgehayfield/PycharmProjects/practical-3/specification-3/templates/homePageHTML.html', 'r+')
    # gets the file path for the spec1 html file and will allow me to display it
    text3 = open('/Users/georgehayfield/PycharmProjects/practical-3/specification-3/templates/spec1.html', 'r+')
    # gets the file path for the spec2 html file and will allow me to display it
    text4 = open('/Users/georgehayfield/PycharmProjects/practical-3/specification-3/templates/spec2.html', 'r+')
    # gets the file path for the spec3 html file and will allow me to display it
    text5 = open('/Users/georgehayfield/PycharmProjects/practical-3/specification-3/templates/spec3.html', 'r+')
    # gets the file path for the spec4 html file and will allow me to display it
    text6 = open('/Users/georgehayfield/PycharmProjects/practical-3/specification-3/templates/spec4.html', 'r+')
    # sets a variable content to text
    content = text.read()
    content1 = text1.read()
    content2 = text2.read()
    content3 = text3.read()
    content4 = text4.read()
    content5 = text5.read()
    content6 = text6.read()
    # renders the spec2.html file
    return render_template("spec3.html", text=content, text1=content1, text2=content2, text3=content3, text4=content4,
                           text5=content5, text6=content6)

# binds a URL to the fourth function
@app.route('/fourth')
# defines the fourth function, anything outside will be rendered in the browser
def fourth():
    # gets the file path for spec4 and will allow me to display it
    text = open('/Users/georgehayfield/PycharmProjects/practical-3/specification-4/web_scraping_olly'
                '/web_scraping_olly.py', 'r+')
    # sets a variable content to text
    content = text.read()
    # renders the spec4.html file
    return render_template("spec4.html", text=content)


# takes the name of the current module as an argument
if __name__ == '__main__':
    # runs the application of the local development server
    # setting debug to true will give more in depth error report
    app.run(debug=True)
