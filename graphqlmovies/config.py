import environ


@environ.config(prefix="")
class Config(object):
    mongo_host = environ.var("0.0.0.0")
    mongo_port = environ.var(27017, converter=int)
    mongo_db = environ.var("graphql-movies")


settings = environ.to_config(Config)
