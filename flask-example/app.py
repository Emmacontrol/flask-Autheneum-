from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/register')
def register():
    return 'Please register!'

@app.route('/login')
def login():
    return 'Please login!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')