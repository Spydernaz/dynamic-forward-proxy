# app.py
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world! I am flask 2'
@app.route('/flask2')
def hello_world_slash():
    return 'Hello world! I am flask 2, the / kind ;)'
if __name__ == '__main__':
    app.run(host='0.0.0.0')

