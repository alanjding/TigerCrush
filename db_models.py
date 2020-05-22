# -------------------------------------------------------------------------------
# db_models.py
# Author: Oleg Golev  (Princeton '22, CS BSE)
#
# Defines database models in SQLAlchemy.
# -------------------------------------------------------------------------------

from app import app
from flask_sqlalchemy import SQLAlchemy

# -------------------------------------------------------------------------------

# -------------- !!! COMMENT OUT IF RUNNING ON HEROKU !!! -------------- #
# DB_URL = "postgresql+psycopg2://{0}:{1}@{2}/{3}".format(USER, PW, HOST, DB_NAME)
# app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
# ---------------------------------------------------------------------- #

# --------------- !!! COMMENT OUT IF RUNNING LOCALLY !!! --------------- #
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
# ---------------------------------------------------------------------- #

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app, engine_options={'pool_pre_ping': True})

class User(db.Model):

    __tablename__ = 'user'

    netid = db.Column(db.String, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    year = db.Column(db.String, nullable=False)
    visible = db.Column(db.Boolean, nullable=False, default=True)
    # contact_info = db.Column(JSON)

    def __repr__(self):
        return f"User('{self.netid}', '{self.name}', '{self.year}', Visible: '{self.visible}')"

# -------------------------------------------------------------------------------

class Crush(db.Model):

    __tablename__ = 'crush'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    crushing = db.Column(db.String, nullable=False)
    crushed_on = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"Crush('{self.id}', '{self.crushing}' crushing on '{self.crushed_on}')"

# -------------------------------------------------------------------------------
