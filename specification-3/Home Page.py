from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    return '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Home Page - Group</title>
            <style>
            body {
            margin: 0;
            font-family: Arial, Helvetica, sans-serif;
            }

            .navigation {
            overflow: hidden;
            background-color: #263859;
            }

            .navigation a {
            float: left;
            color: #f2f2f2;
            text-align: center;
            padding: 14px 16px;
            text-decoration: none;
            font-size: 17px;
            }

            .navigation a:hover {
            background-color: #ddd;
            color: black;
            }

            .navigation a.active {
            background-color: #ff6768;
            color: white;
            }
            body{
            background-color: #6b778d
            }
        </style>
        </head>
        <div class="navigation">
            <a class="active" href="#home">Home</a>
            <a href="#spec1">Specification 1</a>
            <a href="#spec2">Specification 2</a>
            <a href="#spec4">Specification 4</a>
        </div>
        
        <div id="spec4">
            <h3>Got Here </h3>
        </div>
        
        <body>
            <center>
            <h1>Home Page</h1>
            </center>
            <h2>Admin Log-In</h2>
            <button>
             Sign Up
             </button>
        </body>

    </html>'''

if __name__ == '__main__':
    app.run(debug=True)
