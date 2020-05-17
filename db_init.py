# -------------------------------------------------------------------------------
# db_init.py
# Authors: Oleg Golev  (Princeton '22, CS BSE)
#          Jerry Huang (Princeton '22, EE BSE)
#
# Main script that initializes the database. Uses the TigerBook API to fill in
# all entries within the User table. If a user specified custom contact
# that data cannot be overwritten. In either case, it drops the entire Crushes
# table, clearing all previous records of matches and crushes.
#
# The tables are defined in the corresponding db_models.py module with SQLAlchemy.
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
from app import db
from db_models import User, Crush
from db_functions import addUser
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
#                                   STEP 1
# Drop all previous crush data.
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
#                                   STEP 2
# Initialize an HTTP connection to the TigerBook API server URL
# send GET /api/v1/undergraduates to get a JSON of student info
# please see details at: https://github.com/alibresco/tigerbook-api
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
#                                   STEP 3
# Make User entries with the necessary fields to database by calling addUser()
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
