# -------------------------------------------------------------------------------
# db_create.py
# Authors: Oleg Golev  (Princeton '22, CS BSE)
#
# Create the database structure on an existing schema. This must run only once
# to define the tables on an existing empty PostgreSQL schema.
# -------------------------------------------------------------------------------

from app import db
from db_models import User, Crush   # ignore the unused import statement warning

# -------------------------------------------------------------------------------

db.drop_all()
db.create_all()
db.session.commit()

# -------------------------------------------------------------------------------
