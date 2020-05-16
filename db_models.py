# -------------------------------------------------------------------------------
# db_models.py
# Author: Oleg Golev  (Princeton '22, CS BSE)
#
# Defines database models in SQLAlchemy.
# -------------------------------------------------------------------------------

# from datetime import datetime
# from app import db
# from sqlalchemy.dialects.postgresql import JSON

# -------------------------------------------------------------------------------

class User(db.Model):

    __tablename__ = 'user'

    netid = db.Column(db.String(20), primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    year = db.Column(db.String(10), nullable=False)
    visible = db.Column(db.Boolean, nullable=False, default=True)
    contact_info = db.Column(db.JSON)

    def __repr__(self):
        return f"User('{self.netid}', '{self.name}', '{self.year}', Visible: '{self.visible}')"

# -------------------------------------------------------------------------------

class Crush(db.Model):

    __tablename__ = 'crush'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    crushing = db.Column(db.String(20), nullable=False)
    crushed_on = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Crush('{self.id}', '{self.crushing}' crushing on '{self.crushed_on}')"

# -------------------------------------------------------------------------------