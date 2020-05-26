from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, this is a test for Docker image hosting on Heroku.'
