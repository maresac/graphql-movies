def test_query_actors(client, faker):
    actors = [faker.create_actor() for _ in range(5)]
    query = """
        query ActorsQuery {
            actors {
                firstName
                lastName
            }
        }

    """
    response = client.execute(query)
    for i, r in enumerate(response["data"]["actors"]):
        assert actors[i].first_name == r["firstName"]
        assert actors[i].last_name == r["lastName"]


def test_query_directors_last_name(client, faker):
    directors = [faker.create_director() for _ in range(5)]
    query = """
        query DirectorsQuery {
            directors {
                lastName
            }
        }

    """
    response = client.execute(query)
    for i, r in enumerate(response["data"]["directors"]):
        assert directors[i].last_name == r["lastName"]


def test_create_movie(client, faker):
    title = "banana"
    director_first_name = "kitty"
    director_last_name = "cat"

    mutation = """
        mutation CreateMovie {
            createMovie(title: "%s", directorFirstName: "%s", directorLastName: "%s") {
                movie {
                    title
                    director {
                        firstName
                        lastName
                    }
                }
                success
            }

        }

    """ % (
        title,
        director_first_name,
        director_last_name,
    )

    response = client.execute(mutation)
    assert response["data"]["createMovie"]["success"] is True
    movie_response = response["data"]["createMovie"]["movie"]
    assert movie_response["title"] == title
    assert movie_response["director"]["firstName"] == director_first_name
    assert movie_response["director"]["lastName"] == director_last_name
    assert response
