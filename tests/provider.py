from faker.providers import BaseProvider

from graphqlmovies.factories import ActorFactory
from graphqlmovies.factories import DirectorFactory
from graphqlmovies.factories import MovieFactory


class ModelProvider(BaseProvider):
    actors = ActorFactory
    directors = DirectorFactory
    movies = MovieFactory

    def create_actor(self):
        return self.actors.create()

    def create_director(self):
        return self.directors.create()

    def create_movie(self):
        return self.movies.create()
