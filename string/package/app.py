# app.py
from flask import Flask, request, abort
app = Flask(__name__)
@app.route('/')
@app.route('/info')
def describe():
    return 'Converts a string to /uppercase or /lowercase. Takes an argument "string"'


@app.route('/uppercase', methods=['GET', 'POST'])
def uppercase_method():
    try:
        msg = (str)(request.args['string'])
        result = (msg.upper())
        return (result)
    except Exception as e:
        abort(500)



@app.route('/lowercase', methods=['GET', 'POST'])
def lowercase_method():
    try:
        msg = (str)(request.args['string'])
        result = (msg.lower())
        return (result)
    except Exception as e:
        abort(500)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

