from flask import Flask
from flask_graphql import GraphQLView

from graphqlmovies.config import settings
from graphqlmovies.db import connect
from graphqlmovies.db import populate_db
from graphqlmovies.schemas import schema


connect(settings)
populate_db()

app = Flask(__name__)

app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True),
)


@app.route("/")
def index():
    return "Go to /graphql"


if __name__ == "__main__":
    app.run("0.0.0.0")
