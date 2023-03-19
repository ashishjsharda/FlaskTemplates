from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    user = {'username': 'Ashish'}
    return '''
    <html>
        <head>
            <title>Home Page</title>
        </head>
        <body>
            <h1>Hello, ''' + user['username'] + '''!</h1>
        </body>
    </html>'''



if __name__ == '__main__':
    app.run()
