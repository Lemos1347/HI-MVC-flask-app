from src import db
from sqlalchemy.sql import expression

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, server_default=expression.false(), nullable=False)
    # owner_of = db.relationship("realty", backref=db.backref("owner_of", uselist=True))

    def dict(self) -> dict:
        return {"id": self.id, "user_name": self.name, "email": self.email, "password": self.password, "is_admin": self.is_admin}

    def __repr__(self) -> str:
        return str({"id": self.id, "user_name": self.name, "email": self.email, "password": self.password, "is_admin": self.is_admin})
