import csv
import math

            #Step 1
# Find all ratings for a movie by id
# Find the average rating for a movie by id
# Find the name of a movie by id
# Find all ratings for a user

class User:
    def __init__(self, user_id, age, gender, job, zip_code):
        self.user_id = user_id
        self.age = age
        self.gender = gender
        self.job = job
        self.zip_code = zip_code

    def __repr__(self):
        return "User ID: " + self.user_id + " age: " + self.age


class Movie:
    def __init__(self, name, movie_id):
        self.name = name
        self.movie_id = movie_id

    def get_name(self, movie_id):
        return self.title

    def __repr__(self):
        return self.title[:-7]


class Rating:
    def __init__(self, user_id, movie_id, rating):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating

    def __repr__(self):
        return self.rating + " " + self.user_id + " " + self.movie_id

            #Step 2
#You need to be able to load in movie and rating data. Using the csv module,
# write a module that will load in the the user data from u.user, the movie data
# from u.item, and the rating data from u.data.

def load_data_user():
    with open("ml-100k/u.data", encoding= 'latin_1') as data_file:
        data_reader = csv.DictReader(data_file, fieldnames= ['user_id', 'item_id', 'rating', 'timestamp'],  delimiter='\t')
        user_rating_dict = {}
        for row in data_reader:
            user_rating_dict.setdefault(row["user_id"], []).append(row['item_id'])
        return user_rating_dict


def load_user_data():
    with open("ml-100k/u.user",  encoding= 'latin_1') as f:
        user_reader = csv.DictReader(f, delimiter= "|")
        user_dict = {}
        for row in user_reader:
            user_dict[row['user_id']] = User(**row)
        return user_dict


#creates dictionary organized by movie id
def load_movie_data():
    with open("ml-100k/u.item", encoding= 'latin_1') as movie_file:
        movie_reader = csv.DictReader(movie_file, delimiter= "|")
        movie_dict = {}
        for row in movie_reader:
            movie_dict[row["movie_id"]] = Movie(**row)
        #print(movie_dict)
        return movie_dict

#creates dictionary organized by item id
def load_ratings():
    with open("ml-100k/u.data", encoding= 'latin_1') as data_file:
        data_reader = csv.DictReader(data_file, fieldnames= ['user_id', 'item_id', 'rating'],  delimiter='\t')
        item_rating_dict = {}
        for row in data_reader:
            item_rating_dict.setdefault(row["item_id"], []).append(int(row['rating']))
        # print(item_rating_dict)
        return item_rating_dict


                #Step 3
# Write a program to show the top X movies by average rating with their rating.
# You need to be able to state a minimum number of ratings for a movie to be considered.

# Now, create the ability to find the top X movies by average rating that a
# specific user has not rated. This allows you to suggest popular movies for a specific user.

            #Step 4
# create the ability to take two users and find their similarity using the Euclidean distance.
# use this specific formula when you get thereself.

    # def euclidean_distance(v, w):
    #     """Given two lists, give the Euclidean distance between them on a scale
    #     of 0 to 1. 1 means the two lists are identical.
    #     """
    #
    #     # Guard against empty lists.
    #     if len(v) is 0:
    #         return 0
    #
    #     # Note that this is the same as vector subtraction.
    #     differences = [v[idx] - w[idx] for idx in range(len(v))]
    #     squares = [diff ** 2 for diff in differences]
    #     sum_of_squares = sum(squares)
    #
    #     return 1 / (1 + math.sqrt(sum_of_squares))

            #Step 5
# Given a list of all users, find the users most similar to a specific user, and
# then recommend the highest rated movies from those users that the specific user hasn't seen.
#
# A good formula for figuring out movies that user might like the most is similarity * rating.

def main():
    pass
