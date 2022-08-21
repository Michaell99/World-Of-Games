from flask import Flask, render_template
import templates
import os


app = Flask(__name__)
app.static_folder = 'static'


def safe_cast(val, to_type, default=None):
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default


@app.route('/')
def score_server():
    res = 0
    score_file = open('static/score.txt', 'r')
    score = score_file.readline()
    if score == "":
        return render_template('scoreError.html', Error="Can't open file"), 400
    elif score != res:
        res = res + safe_cast(score, int, 0)
        return render_template('Score.html', SCORE=res), 200

app.run('0.0.0.0', debug=True, port=30000)
