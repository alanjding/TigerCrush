# -------------------------------------------------------------------------------
# db_init.py
# Authors: Alan Ding   (Princeton '22, CS BSE)
#          Oleg Golev  (Princeton '22, CS BSE)
#
# Main script that initializes the database. Uses the TigerBook API to fill in
# all entries within the User table. If a user specified custom contact
# that data cannot be overwritten. In either case, it drops the entire Crushes
# table, clearing all previous records of matches and crushes.
#
# The script is to be run ONLY at the beginning of each run through heroku run.
#
# The tables are defined in the corresponding db_models.py module with SQLAlchemy.
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
# click is a library that enables us to run Python scripts on Heroku
import click
from flask.cli import with_appcontext
from app import db
import os
import hashlib
import random
from base64 import b64encode
from datetime import datetime
import requests
import json
from db_functions import addUser
# -------------------------------------------------------------------------------

# resets the database such that it consists of just a list of students and no
# crushes between any two students
@click.command(name='resetDB')
@with_appcontext
def resetDB():
    print('Deleting existing data... ', end='')

    # drop all previous crush data
    db.drop_all()
    db.create_all()
    db.session.commit()

    print('Done!')
    print('Fetching students from TigerBook... ', end='')

    # grab TigerBook data
    students = getStudents()

    print('Done!')
    print('Populating database with student data... ', end='')

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
    password = 'cedda4cc61fe1c736aada24eda32f5ab'
    # password = os.environ.get('TIGERBOOK_KEY')
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

# -------------------------------------------------------------------------------