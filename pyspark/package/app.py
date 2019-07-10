# app.py
from flask import Flask, request
from data.data_source import DataSource

app = Flask(__name__)
@app.route('/')
@app.route('/info')
def describe():
    return 'Test PySpark Job :). Call it by running the job /pytest and passing the paramater \"p\"'


@app.route('/pytest', methods=['GET', 'POST'])
@app.route('/upper/pytest', methods=['GET', 'POST'])
@app.route('/jobs/upper/pytest', methods=['GET', 'POST'])
def test():
    try:
        msg = request.args['p']
        src = DataSource()
        df = src.get_data(num_elements=1000000)
        print("Got Pandas dataframe with {} elements, top 10:".format(df.size))
        print(df.head(10))
    except Exception as e:
        result = "Something failed? {}".format(e)
    finally:
        return (result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

