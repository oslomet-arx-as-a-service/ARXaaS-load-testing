import string
import random


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
