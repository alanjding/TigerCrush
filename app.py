# -------------------------------------------------------------------------------
# app.py
# Authors: Alan Ding   (Princeton '22, CS BSE)
#          Oleg Golev  (Princeton '22, CS BSE)
#
# Running module and the routing middle-tier.
# -------------------------------------------------------------------------------

from flask import *
from sys import argv, stderr
from db_functions import *
import os
import hashlib
import random
from base64 import b64encode
from datetime import datetime
import requests
import json

# -----------------------------------------------------------------------
#                         APP AND DATABASE SETUP
# -----------------------------------------------------------------------

from private import USER, PW, HOST, DB_NAME

appl = Flask(__name__, template_folder="templates", static_folder="static")
appl.secret_key = b'\n\x10_\xbdxBq)\xd7\xce\x80w\xbcr\xe2\xf3\xdclo\x1e0\xbadZ'

# -----------------------------------------------------------------------
#                           PER-REQUEST SETUP
#                 !!! COMMENT OUT IF RUNNING LOCALLY !!!
# -----------------------------------------------------------------------

@appl.before_request
def redirectHTTP():
    # redirect http to https
    if request.url[0:5] != 'https':
        return redirect(request.url.replace('http', 'https', 1))

# -----------------------------------------------------------------------
#                         PAGE ROUTING SECTION
# -----------------------------------------------------------------------

@appl.route('/')
@appl.route('/login')
def login():
    html = render_template("login.html")
    return make_response(html)

# -----------------------------------------------------------------------

@appl.route('/index')
def index():
    # temporary, will need to be replaced by CAS functionality and storing state
    # that says who's logged in as opposed to passing in a username as a request
    # argument
    netid = 'guest'
    if 'netid' in request.args:
        netid = request.args.get('netid')
    # end temporary stuff

    remCrushes = getRemCrushes(netid)
    numSecretAdmirers = getSecretAdmirers(netid)

    html = render_template("index.html",
                           netid=netid,
                           remCrushes=remCrushes,
                           numSecretAdmirers=numSecretAdmirers)
    return make_response(html)

# -----------------------------------------------------------------------

@appl.route('/faq')
def faq():
    html = render_template("faq.html")
    return make_response(html)

# -----------------------------------------------------------------------

@appl.route('/about')
def about():
    html = render_template("about.html")
    return make_response(html)

# -----------------------------------------------------------------------
#                        ENDPOINTS FOR REQUESTS
# -----------------------------------------------------------------------

# helper endpoint that returns formatted Tigerbook data
@appl.route('/studentInfo')
def studentInfo():
    return {'data': getFormattedStudentInfoList()}

# -----------------------------------------------------------------------

# gets and formats (into a list of strings to be displayed) the crushes
# for the user with the specified netid
@appl.route('/getCrushes')
def crushes():
    crushList = getCrushes(request.args.get('netid'))
    return {'data': [getName(crush.crushed_on) for crush in crushList]}

# -----------------------------------------------------------------------

# gets and formats (into a list of strings to be displayed) the matches
# for the user with the specified netid
@appl.route('/getMatches')
def matches():
    matchList = getMatches(request.args.get('netid'))
    return {'data': [getName(match.crushing) for match in matchList]}

# -----------------------------------------------------------------------

# adds a crush (crushNetid arg) for a given user (netid arg)
@appl.route('/addCrush', methods=['GET', 'POST'])
def addCrushEndpoint():
    if request.method == 'POST':
        netid = request.form.get('netid')
        crushNetid = request.form.get('crushNetid')
        crushNetid = crushNetid.split(' ', 1)[0]

        print('addCrush netid argument value: ' + netid)
        print('addCrush crushNetid argument value: ' + crushNetid)

        matched = addCrush(netid, crushNetid)
        print(matched)

        # TODO - send email if matched

    # TODO - this is just placeholder code! Will need to be changed according to
    # how CAS sets authorization cookies
    return redirect(url_for('index'))

# -----------------------------------------------------------------------
#                   DATABASE INITIALIZATION COMMANDS
# -----------------------------------------------------------------------

# resets the database such that it consists of just a list of students and no
# crushes between any two students
@appl.cli.command(name='resetDB')
def resetDB():
    print('Deleting existing data... ', end='', flush=True)

    # drop all previous crush data
    db.drop_all()
    db.create_all()
    db.session.commit()

    print('Done!')
    print('Fetching students from TigerBook... ', end='', flush=True)

    # grab TigerBook data
    students = getStudents()

    print('Done!')
    print('Populating database with student data... ', end='', flush=True)

    # create rows in the db for each student
    for student in students:
        netid = student['net_id']
        name = student['full_name']
        year = student['class_year']
        addUser(netid, name, year)

    print('Done!')

# -------------------------------------------------------------------------------

# helper function that returns a Python dict of data grabbed from TigerBook
def getStudents():
    url = 'https://tigerbook.herokuapp.com/api/v1/undergraduates'
    created = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    nonce = ''.join([random.choice(
        '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/') for
        i in range(32)])
    username = 'ajding'
    password = os.environ.get('TIGERBOOK_KEY')
    generated_digest = b64encode(hashlib.sha256(
        nonce.encode('utf-8') + created.encode('utf-8') + password.encode(
            'utf-8')).digest()).decode()
    headers = {
        'Authorization': 'WSSE profile="UsernameToken"',
        'X-WSSE': 'UsernameToken Username="%s", PasswordDigest="%s", Nonce="%s", Created="%s"' % (
            username, generated_digest, b64encode(nonce.encode()).decode(),
            created)
    }

    r = requests.get(url, headers=headers)
    return json.loads(r.text)

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

    appl.run(host="0.0.0.0", port=int(argv[1]))

# -----------------------------------------------------------------------
