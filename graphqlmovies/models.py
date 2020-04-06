from mongoengine import Document
from mongoengine.fields import DateTimeField
from mongoengine.fields import ListField
from mongoengine.fields import ReferenceField
from mongoengine.fields import StringField


class Actor(Document):
    meta = {"collection": "actor"}
    first_name = StringField(required=True)
    last_name = StringField(required=True)


class Director(Document):
    meta = {"collection": "director"}
    first_name = StringField(required=True)
    last_name = StringField(required=True)


class Movie(Document):
    meta = {"collection": "movie"}
    title = StringField(required=True)
    director = ReferenceField(Director, required=True)
    actors = ListField(ReferenceField(Actor))
    release_date = DateTimeField()
