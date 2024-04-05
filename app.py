from flask import Flask
app = Flask(__name__)

# Flast listens on port 5000 by default
@app.route('/')
def hello_world():
    return 'Hello, Docker!'