import string
import random
import pandas as pd


def test_dataset(row_count):
    raw_data = {"id": [id for id in range(row_count)],
                "name": [random_string() for _ in range(row_count)],
                "age": [generate_age() for _ in range(row_count)],
                "gender": [generate_genders() for _ in range(row_count)],
                "location": [generate_location() for _ in range(row_count)]}
    return raw_data


def random_string(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def generate_genders():
    genders = ("male", "female")
    return random.choice(genders)


def generate_age():
    return random.randint(10, 101)


def generate_location():
    locations = ("Oslo", "Bergen", "London", "Miami", "Tokyo", "Bejing", "Moscow")
    return random.choice(locations)


def gender_hierarchy():
    return [["male","*"],
            ["female","*"]]


def age_hierarchy():
    level_0 = [age for age in range(10,102)]
    level_1 = ["]10,101[" for _ in range(10,102)]
    hir = zip(level_0, level_1)
    return [[str(row[0]), row[1]] for row in hir]


def name_hierarchy():
    return pd.read_csv("hierarchies/name_hierarchy.csv", sep=",", header=None)


def location_hierarchy():
    return pd.read_csv("hierarchies/location_hierarchy.csv", sep=",", header=None)



