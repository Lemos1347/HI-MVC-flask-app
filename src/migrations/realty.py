from src import db


class Realty(db.Model):
    __tablename__ = 'realty'
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def dict(self) -> dict:
        return {"id": self.id, "name": self.name, "description": self.description, "owner_id": self.owner_id}

    def __repr__(self) -> str:
        return str({"id": self.id, "name": self.name, "description": self.description, "owner_id": self.owner_id})
