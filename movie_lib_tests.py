from movie_lib import *



def test_user_list():
    assert all_users == {1:User(1),2:User(2), 3:User(3)}


def test_movie_list():
    # print(all_movies)
    assert all_movies == {1:Movie(1, 'Toy Story', 'genre'), 1682:Movie(1682, 'Scream of Stone', 'genre')}
