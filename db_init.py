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
from app import db, app
import os
import hashlib
import random
from base64 import b64encode
from datetime import datetime
import requests
import json
from db_functions import addUser
# -------------------------------------------------------------------------------

