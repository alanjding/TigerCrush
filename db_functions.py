# -------------------------------------------------------------------------------
# db_functions.py
# Authors: Oleg Golev  (Princeton '22, CS BSE)
#          Jerry Huang (Princeton '22, EE BSE)
#
# Defines back-end API for enabling dynamic manipulation of the website front end.
# -------------------------------------------------------------------------------

# from app import db
# from db_models import User, Crush
# import json

# -------------------------------------------------------------------------------
#                                 addUser()
# -------------------------------------------------------------------------------
# Add a user to the database. There are two uses.
# (1) Helper function for initializing the database in db_init.py
# (2) If the user is not an undergraduate or is not on TigerBook, let the user
#     add themselves to the system manually. year field will be "GRAD" if it is
#     a graduate student, "STAFF" if it is a professor or a post-doc researcher.
#
# Upon success, return 0. Upon failure, print a descriptive error and return a
# user-readable error to display on the web page.
# -------------------------------------------------------------------------------

def addUser(netid, name, year):
    pass

# -------------------------------------------------------------------------------
#                                 addCrush()
# -------------------------------------------------------------------------------
# Take two netid's represented as strings to add a new entry to the crush table.
# Call attemptMatch() executing in a new thread before returning.
#
# Upon success, return 0. Upon failure, print a descriptive error and return a
# user-readable error to display on the web page.
# -------------------------------------------------------------------------------

def addCrush(crushing, crushed_on):
    pass

# -------------------------------------------------------------------------------
#                               attemptMatch()
# -------------------------------------------------------------------------------
# Checks whether there are two inverse entries in the crush table. If so, a match
# has been found. Send a one-time email with contact information to the two users.
#
# Upon success, return 0. Upon failure, print a descriptive error and return a
# user-readable error to display on the web page.
# -------------------------------------------------------------------------------

def attemptMatch(netid11, netid2):
    pass

# -------------------------------------------------------------------------------
#                                  getCrushes()
# -------------------------------------------------------------------------------
# Retrieve (by netid) a user's crushes as a list of dictionaries with fields:
#   netid: ""
#   name: ""
#   year: (int)
#
# Upon failure, print a descriptive error and return a ser-readable error to
# display on the web page.
# -------------------------------------------------------------------------------

def getCrushes(netid):
    pass

# -------------------------------------------------------------------------------
#                                  getMatches()
# -------------------------------------------------------------------------------
# Retrieve (by netid) a user's matches as a list of dictionaries with fields:
#   netid: ""
#   name: ""
#   year: (int)
#
# Upon failure, print a descriptive error and return a ser-readable error to
# display on the web page.
# -------------------------------------------------------------------------------

def getMatches(netid):
    pass

# -------------------------------------------------------------------------------
#                              getMaxCrushes()
# -------------------------------------------------------------------------------
# Retrieve the maximum number of crushes that a given person may have. For this
# application, this is 5 + 1 for each secret admirer.
#
# Upon success, return the maximum number of crushes. Upon failure, print a
# descriptive error and return a ser-readable error to display on the web page.
# -------------------------------------------------------------------------------

def getMaxCrushes(netid):
    pass

# -------------------------------------------------------------------------------
#                              getSecretAdmirers()
# -------------------------------------------------------------------------------
# Retrieve the number of secret admirers that a given person has.
#
# Upon success, return the number of admirers. Upon failure, print a descriptive
# error and return a ser-readable error to display on the web page.
# -------------------------------------------------------------------------------

def getSecretAdmirers(crushing, crushed_on):
    pass

# -------------------------------------------------------------------------------
#                               UTILITY FUNCTIONS
# -------------------------------------------------------------------------------
# Getters and setters for custom contact information of the application users.
#
# For more information on how to query PostgreSQL JSON dictionaries and how to
# convert them to Python dictionaries, please refer to...
# https://stackoverflow.com/questions/23878070/using-json-type-with-flask-sqlalchemy-postgresql
#
# For more information on how to access JSON fields in PostgreSQL tables, read
# https://stackoverflow.com/questions/50043077/flask-sqlalchemy-mysql-json-column-update-not-working
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------