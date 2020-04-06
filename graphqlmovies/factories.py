from random import randint

import factory
from faker import Factory

from graphqlmovies.models import Actor
from graphqlmovies.models import Director
from graphqlmovies.models import Movie


faker = Factory.create()


class ActorFactory(factory.mongoengine.MongoEngineFactory):
    class Meta:
        model = Actor

    @factory.lazy_attribute
    def first_name(self):
        return faker.first_name()

    @factory.lazy_attribute
    def last_name(self):
        return faker.last_name()


class DirectorFactory(factory.mongoengine.MongoEngineFactory):
    class Meta:
        model = Director

    @factory.lazy_attribute
    def first_name(self):
        return faker.first_name()

    @factory.lazy_attribute
    def last_name(self):
        return faker.last_name()


class MovieFactory(factory.mongoengine.MongoEngineFactory):
    class Meta:
        model = Movie

    @factory.lazy_attribute
    def title(self):
        return "{} {}".format(faker.color_name(), faker.first_name())

    @factory.lazy_attribute
    def director(self):
        return DirectorFactory.create()

    @factory.lazy_attribute
    def actors(self):
        return ActorFactory.create_batch(randint(2, 10))

    @factory.lazy_attribute
    def release_date(self):
        return faker.date()
