from faker import Factory
from graphene.test import Client
from mongoengine import connect
import pytest

from graphqlmovies.schemas import schema
from tests.provider import ModelProvider


@pytest.fixture
def connection():
    db = connect("graphql-movies", alias="default")
    db.drop_database("graphql-movies")


@pytest.fixture
def faker(connection):
    faker = Factory.create()
    faker.add_provider(ModelProvider)
    return faker


@pytest.fixture
def client():
    return Client(schema=schema)
