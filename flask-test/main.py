from flask import Flask
from json import dumps

app = Flask(__name__)  # notice that the app instance is called `app`, this is very important.

@app.route("/")
def hello_world():
    return dumps({"message": "Hello, world!"})