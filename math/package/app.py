# app.py
from flask import Flask, request, abort

app = Flask(__name__)
@app.route('/')
@app.route('/info')
def describe():
    return 'This server provides 3 methods; /double, /square and /increment (add on). All 3 take a parameter call "n"'


@app.route('/double', methods=['GET', 'POST'])
def double():
    try:
        number = (int)(request.args['n'])
        result = number + number
        return (str(result))
    except:
        abort(500)


@app.route('/square', methods=['GET', 'POST'])
def square():
    try:
        number = (int)(request.args['n'])
        result = number * number
        return (str(result))
    except:
        abort(500)



@app.route('/increment', methods=['GET', 'POST'])
def increment():
    try:
        number = (int)(request.args['n'])
        result = number + 1
        return (str(result))
    except:
        abort(500)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

