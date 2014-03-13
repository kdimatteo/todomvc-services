from flask import g
from flask import request
from flask import json
import flask
import os
from functools import wraps
import sqlite3


app = flask.Flask(__name__)

DATABASE = 'todo.db'

def connect_db():
    return sqlite3.connect(DATABASE)

@app.before_request
def before_request():
    g.db = connect_db()

@app.after_request
def after_request(response):
    g.db.close()
    return response

@app.route("/api/todos", methods=['GET'])
def getData():
    cur = g.db.execute('''SELECT title, is_completed FROM todos''')
    rv = [dict((cur.description[idx][0], value)
                for idx, value in enumerate(row)) for row in cur.fetchall()]
    return json.dumps(rv)

@app.route("/api/todos", methods=['POST'])
def postData():
    
    o = flask.request.data #.form['title']
    c = g.db.execute("INSERT INTO todos ('is_completed', 'title') VALUES (?, ?)", (flask.request.json['isCompleted'], flask.request.json['title']))
    g.db.commit()
    
    # insert the new ID and return the data
    flask.request.json['id'] = c.lastrowid
    return json.dumps(flask.request.json)
    
if __name__ == "__main__":
	# Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port, debug=True)