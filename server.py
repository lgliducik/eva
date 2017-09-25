import sys
import os
import logging

from flask import Flask, request
from flask import render_template, request, url_for, redirect, session
from database import DB_CONNECTOR, ORM

app = Flask(__name__)

logger = logging.getLogger(__name__)
logging.basicConfig(stream = sys.stdout, level=logging.DEBUG)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONNECTOR
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
logger.info('create db')
db = ORM(app)


logger = logging.getLogger(__name__)
		
		
@app.route("/addaction", methods=["POST"])
def addaction():
    if request.method == "POST":
        name = request.form.get("name")
        freq = request.form.get("freq")
        db.add_action(name, freq)
        return redirect(url_for("showaction"))
		
		
@app.route("/delaction", methods=["GET"])
def delaction():
    if request.method == "GET":
        return "Hello"
		
		
@app.route("/showaction", methods=["GET", "POST"])
def showaction():
    if request.method == "GET":
        actions = db.all_actions()
        print actions
        return render_template('hello.html', actions=actions)
    if request.method == "POST":
        name = request.form.get("name")
        freq = request.form.get("freq")
        db.add_action(name, freq)
        return redirect(url_for("showaction"))
		

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    app.run(port=int(os.environ.get("PORT", 5000)))
