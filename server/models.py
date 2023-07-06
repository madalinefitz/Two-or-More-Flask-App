from sqlalchemy_serializer import SerializerMixin
from config import db
from sqlalchemy.orm import validates


class Story(db.Model, SerializerMixin):
    __tablename__ = 'stories'

    id = db.Column(db.Integer, primary_key = True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name_initial = db.Column(db.String, nullable=False)
    story = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
