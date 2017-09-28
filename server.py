import sys
import os
import logging
import json
import datetime

from flask import Flask, request
from flask import render_template, request, url_for, redirect, session

from database import DB_CONNECTOR, ORM


app = Flask(__name__)

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONNECTOR
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
logger.info('create db')
db = ORM(app)
logger = logging.getLogger(__name__)


@app.route("/add_action", methods=["POST"])
def add_action():
    if request.method == "POST":
        data = json.loads(request.data)
        name = data['name']
        freq = data['freq']
        db.add_action(name, freq)
        return redirect(url_for("show_actions"))


# пример запроса /del_action?name=sport
@app.route("/del_action", methods=["DELETE"])
def del_action():
    if request.method == "DELETE":
        name_action = request.args.get('name')
        db.delete_action(name_action)
        return "delete " + name_action + " from db"


@app.route("/add_point", methods=["POST"])
def add_point():
    if request.method == "POST":
        data = json.loads(request.data)
        name = data['name']
        date_str = data['date']
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        db.add_point(name, date)
        return "add point action:" + name + "date:" + date_str


# пример запроса /show_week?start=2017-09-25&end=2017-09-28
@app.route("/show_week", methods=["GET"])
def show_week():
    if request.method == "GET":
        start = request.args.get('start')
        end = request.args.get('end')
        actions_per_week = db.all_points_interval(start, end)
        print "actions_per_week", actions_per_week
        return "show week"


@app.route("/show_actions", methods=["GET", "POST"])
def show_actions():
    if request.method == "GET":
        actions = db.all_actions()
        return render_template('hello.html', actions=actions)
    if request.method == "POST":
        name = request.form.get("name")
        freq = request.form.get("freq")
        db.add_action(name, freq)
        return redirect(url_for("show_actions"))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    app.run(port=int(os.environ.get("PORT", 5000)))
