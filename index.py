
from Database import DATABASE
import flask 
from flask import render_template, jsonify
from datetime import date
from random import choice

app = flask.Flask(__name__)

@app.route('/today', methods=['GET'])
@app.route('/', methods=['GET'])
def today():
    today = date.today()
    data = DATABASE[str(int(today.month))][str(int(today.day))]
    # print(data, today.month, today.day)
    return render_template('home.html', data=data)

@app.route('/<month>/<day>', methods=['GET'])
def specific(month, day):
    # print(month, day)
    if month not in DATABASE or day not in DATABASE[month]:
        return jsonify({"response": 404, "content": "invalid date"})

    data = DATABASE[month][day]
    return render_template('home.html', data=data)

@app.route('/random', methods=['GET'])
def random():
    month = choice(list(DATABASE.keys()))
    day = choice(list(DATABASE[month].keys()))

    data = DATABASE[month][day]
    return render_template('home.html', data=data)

@app.route('/api/<month>/<day>', methods=['GET'])
@app.route('/api', methods=['GET'])
def api(month=date.today().month, day=date.today().day):
    if str(month) not in DATABASE or str(day) not in DATABASE[str(month)]:
        return jsonify({"response": 404, "content": "invalid date"})

    data = DATABASE[str(month)][str(day)]
    return jsonify(data)

# if __name__ == "__main__":
#    app.run(host='0.0.0.0', port=8080)

