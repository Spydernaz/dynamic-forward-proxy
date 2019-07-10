# app.py
from flask import Flask, request
app = Flask(__name__)
@app.route('/')
@app.route('/info')
def describe():
    return 'I am Flask App 1 - I have a method (/uppercase) for converting to UPPERCASE and take the variable \"String\"'


@app.route('/uppercase', methods=['GET', 'POST'])
@app.route('/upper/uppercase', methods=['GET', 'POST'])
@app.route('/jobs/upper/uppercase', methods=['GET', 'POST'])
def uppercase_method():
    try:
        msg = request.args['string']
        # msg = "a string"
        print (msg)
        result = (msg.upper())
    except Exception as e:
        result = "Something failed? {}".format(e)
    finally:
        return (result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

