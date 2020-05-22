# -------------------------------------------------------------------------------
# db_functions.py
# Authors: Alan Ding   (Princeton '22, CS BSE)
#          Oleg Golev  (Princeton '22, CS BSE)
#
# Defines back-end API for enabling dynamic manipulation of the website front end.
# -------------------------------------------------------------------------------

from app import db
from db_models import User, Crush

# -------------------------------------------------------------------------------
#                                 addUser()
# -------------------------------------------------------------------------------
# Add a user to the database. There are two uses.
# (1) Helper function for initializing the database
# (2) If the user is not an undergraduate or is not on TigerBook, let the user
#     add themselves to the system manually. year field will be "GRAD" if it is
#     a graduate student, "STAFF" if it is a professor or a post-doc researcher.
#
# Upon success, return 0. Upon failure, print a descriptive error and return a
# user-readable error to display on the web page.
# -------------------------------------------------------------------------------

def addUser(netid, name, year):
    user = User(netid=netid, name=name, year=year, visible=True)
    db.session.add(user)
    db.session.commit()

# -------------------------------------------------------------------------------
#                                 addCrush()
# -------------------------------------------------------------------------------
# Take two netid's represented as strings to add a new entry to the crush table.
# Call attemptMatch() executing in a new thread before returning.
#
# Returns whether the added crush resulted in a match.
# -------------------------------------------------------------------------------

def addCrush(crushing, crushed_on):
    # do nothing if user attempts to crush on themselves
    if crushing == crushed_on:
        return False

    # TODO: do nothing if crush already exists

    crush = Crush(crushing=crushing, crushed_on=crushed_on)
    db.session.add(crush)
    db.session.commit()
    return isMatch(crushing, crushed_on)

# -------------------------------------------------------------------------------
#                                   isMatch()
# -------------------------------------------------------------------------------
# Checks whether there are two inverse entries in the crush table. If so, a match
# has been found. Send a one-time email with contact information to the two users.
#
# Returns whether netid1 and netid2 mutually crush on each other.
# -------------------------------------------------------------------------------

def isMatch(netid1, netid2):
    return netid2 in getCrushNames(netid1) and netid1 in getCrushNames(netid2)

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
    crushes = Crush.query.filter_by(crushing=netid).all()
    print('crushes:')
    print(crushes)
    return crushes

# -------------------------------------------------------------------------------
#                                  getCrushNames()
# -------------------------------------------------------------------------------
# Retrieve (by netid) a user's crushes as a list of netids (strings)
#
# Upon failure, print a descriptive error and return a ser-readable error to
# display on the web page.
# -------------------------------------------------------------------------------

def getCrushNames(netid):
    crushes = getCrushes(netid)
    return [crush.crushed_on for crush in crushes]

# -------------------------------------------------------------------------------
#                                  getName()
# -------------------------------------------------------------------------------
# Returns the name of the student with the given netid
#
# Upon failure, print a descriptive error and return a ser-readable error to
# display on the web page.
# -------------------------------------------------------------------------------

def getName(netid):
    user = db.session.query(User).filter_by(netid=netid).first()
    return "%s, %s" % (user.name, user.year)

# -------------------------------------------------------------------------------
#                                  getMatches()
# -------------------------------------------------------------------------------
# Retrieve (by netid) a user's matches as a list of netids
#
# Upon failure, print a descriptive error and return a ser-readable error to
# display on the web page.
# -------------------------------------------------------------------------------

# TODO: fix
def getMatches(netid):
    myCrushes = getCrushNames(netid)

    crushingOnMeRows = db.session.query(Crush) \
        .filter_by(crushed_on=netid) \
        .all()

    crushingOnMe = [crush.crushing for crush in crushingOnMeRows]
    matches = list(set(myCrushes) & set(crushingOnMe))

    # for debugging purposes only! delete later
    print('matches:')
    print(matches)
    return matches

# -------------------------------------------------------------------------------
#                              getRemCrushes()
# -------------------------------------------------------------------------------
# Retrieve the remaining number of crushes that a given person may have. For
# this application, this is 5 + 1 more for each secret admirer minus the number
# of crushes that the given person already has.
#
# Upon success, return the maximum number of crushes. Upon failure, print a
# descriptive error and return a ser-readable error to display on the web page.
# -------------------------------------------------------------------------------

def getRemCrushes(netid):
    return 5 + getSecretAdmirers(netid) - len(getCrushes(netid))

# -------------------------------------------------------------------------------
#                              getSecretAdmirers()
# -------------------------------------------------------------------------------
# Retrieve the secret admirers that a given person has.
#
# Upon success, return a list of admirers. Upon failure, print a descriptive
# error and return a user-readable error to display on the web page.
# -------------------------------------------------------------------------------

# TODO: fix
def getSecretAdmirers(netid):
    myCrushes = getCrushNames(netid)

    crushingOnMeRows = db.session.query(Crush) \
        .filter_by(crushed_on=netid) \
        .all()

    crushingOnMe = [crush.crushing for crush in crushingOnMeRows]
    secretAdmirers = list(set(crushingOnMe) - set(myCrushes))

    # for debugging purposes only! delete later
    print('secret admirers:')
    print(secretAdmirers)
    return len(secretAdmirers)

# -------------------------------------------------------------------------------
#                         getFormattedStudentInfoList()
# -------------------------------------------------------------------------------
# Returns a dictionary of all students' netids, names, and class years to be
# used by the front-end's autocompletion interface
# -------------------------------------------------------------------------------

def getFormattedStudentInfoList():
    users = User.query.all()
    r = ['%s - %s, %s' % (user.netid, user.name, user.year) for user in users]
    return r

# -------------------------------------------------------------------------------
