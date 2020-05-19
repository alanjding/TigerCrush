# -------------------------------------------------------------------------------
# app.py
# Authors: Alan Ding   (Princeton '22, CS BSE)
#          Oleg Golev  (Princeton '22, CS BSE)
#          Jerry Huang (Princeton '22, EE BSE)
#
# Running module and the routing middle-tier.
# -------------------------------------------------------------------------------

from flask import Flask, render_template, make_response
from sys import argv, stderr
import json
from db_functions import *

# -----------------------------------------------------------------------
#                         APP AND DATABASE SETUP
# -----------------------------------------------------------------------

from private import USER, PW, HOST, DB_NAME

app = Flask(__name__, template_folder="templates", static_folder="static")
DB_URL = "postgresql+psycopg2://{0}:{1}@{2}/{3}".format(USER, PW, HOST, DB_NAME)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = b'\n\x10_\xbdxBq)\xd7\xce\x80w\xbcr\xe2\xf3\xdclo\x1e0\xbadZ'

# -----------------------------------------------------------------------
#                            ROUTING SECTION
# -----------------------------------------------------------------------

@app.route('/')
@app.route('/login')
def login():
    html = render_template("login.html")
    return make_response(html)

# -----------------------------------------------------------------------

@app.route('/index')
def index():
    html = render_template("index.html")
    return make_response(html)

# -----------------------------------------------------------------------

@app.route('/faq')
def index():
    html = render_template("faq.html")
    return make_response(html)

# -----------------------------------------------------------------------

@app.route('/about')
def index():
    html = render_template("about.html")
    return make_response(html)

# -----------------------------------------------------------------------

# helper endpoint that returns formatted Tigerbook data
@app.route('/studentInfo')
def studentInfo():
    return getFormattedStudentInfoList()

# -----------------------------------------------------------------------
#                            MAIN METHOD
# -----------------------------------------------------------------------
# Requires a port number as a command-line argument. Starts the app.
# -----------------------------------------------------------------------

if __name__ == '__main__':

    if len(argv) != 2:
        print("Usage: " + argv[0] + " [port]", file=stderr)
        exit(1)

    try:
        ret = int(argv[1])
    except:
        print("Port must be an integer", file=stderr)
        exit(1)

    app.run(host="0.0.0.0", port=int(argv[1]))

# -----------------------------------------------------------------------
