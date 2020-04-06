import datetime

import graphene
from graphene_mongo import MongoengineObjectType

from graphqlmovies.models import Actor as ActorModel
from graphqlmovies.models import Director as DirectorModel
from graphqlmovies.models import Movie as MovieModel


class Actor(MongoengineObjectType):
    class Meta:
        model = ActorModel


class Director(MongoengineObjectType):
    class Meta:
        model = DirectorModel


class Movie(MongoengineObjectType):
    class Meta:
        model = MovieModel


class CreateActor(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)

    success = graphene.Boolean()
    actor = graphene.Field(lambda: Actor)

    def mutate(self, info, **kwargs):
        actor = ActorModel(**kwargs)
        actor.save()

        return CreateActor(actor=actor, success=True)


class CreateDirector(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)

    success = graphene.Boolean()
    actor = graphene.Field(lambda: Director)

    def mutate(self, info, **kwargs):
        director = DirectorModel(**kwargs)
        director.save()

        return CreateDirector(director=director, success=True)


class CreateMovie(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        director_first_name = graphene.String(required=True)
        director_last_name = graphene.String(required=True)

    success = graphene.Boolean()
    movie = graphene.Field(lambda: Movie)

    def mutate(self, info, **kwargs):
        director = DirectorModel(
            first_name=kwargs.pop("director_first_name"),
            last_name=kwargs.pop("director_last_name"),
        )
        director.save()
        kwargs["director"] = director
        movie = MovieModel(**kwargs)
        movie.release_date = datetime.datetime.now()
        movie.save()

        return CreateMovie(movie=movie, success=True)


class AddActor(graphene.Mutation):
    class Arguments:
        movie_title = graphene.String(required=True)
        actor_first_name = graphene.String(required=True)
        actor_last_name = graphene.String(required=True)

    success = graphene.Boolean()
    movie = graphene.Field(lambda: Movie)

    def mutate(self, info, **kwargs):
        actor = ActorModel(
            first_name=kwargs.pop("actor_first_name"),
            last_name=kwargs.pop("actor_last_name"),
        )
        actor.save()
        movie = MovieModel.objects(title=kwargs.pop("movie_title"))
        if not movie:
            return AddActor(movie=None, success=False)

        movie = movie.first()
        movie.actors.append(actor)
        movie.save()
        return AddActor(movie=movie, success=True)


class Query(graphene.ObjectType):
    actors = graphene.List(Actor)
    directors = graphene.List(Director)
    movies = graphene.List(Movie)

    def resolve_actors(self, info):
        return list(ActorModel.objects.all())

    def resolve_directors(self, info):
        return list(DirectorModel.objects.all())

    def resolve_movies(self, info):
        return list(MovieModel.objects.all())


class Mutations(graphene.ObjectType):
    create_actor = CreateActor.Field()
    create_director = CreateDirector.Field()
    create_movie = CreateMovie.Field()
    add_actor = AddActor.Field()


schema = graphene.Schema(
    query=Query, mutation=Mutations, types=[Actor, Director, Movie]
)
