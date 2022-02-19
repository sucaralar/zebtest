import sqlalchemy.exc
from flask_restx import abort
from application import db


class BaseModel(db.Model):
    """ Abstract BaseModel for Model"""

    __abstract__ = True
    __tablename__ = "base"

    @classmethod
    def first_by(cls, **kwargs) -> db.Model:
        return cls.query.filter_by(**kwargs)

    @classmethod
    def first(cls, criteria: dict) -> db.Model:
        for attr, value in criteria.items():
            query = cls.query.filter(getattr(cls, attr) == value).first()
        return query

    @classmethod
    def get_by_id(cls, _id: int):
        return cls.query.get(_id)

    @classmethod
    def list(cls, *criteria):
        return cls.query.filter(*criteria).all()

    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError as e:
            abort(409, **{"error": "duplicates key"})
        return self

    def update(self, data: dict):
        for field, value in data.items():
            setattr(self, field, value)
        db.session.add(self)
        db.session.commit()
        db.session.refresh(self)
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
