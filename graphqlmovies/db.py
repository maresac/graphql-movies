import mongoengine

from graphqlmovies.factories import ActorFactory
from graphqlmovies.factories import DirectorFactory
from graphqlmovies.factories import MovieFactory


def connect(settings):
    mongoengine.connect(
        settings.mongo_db,
        host=settings.mongo_host,
        port=settings.mongo_port,
        alias="default",
    )


def populate_db():
    ActorFactory.create_batch(20)
    DirectorFactory.create_batch(10)
    MovieFactory.create_batch(7)
