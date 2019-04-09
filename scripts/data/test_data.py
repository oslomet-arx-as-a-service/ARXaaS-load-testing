import string
import pandas as pd
from pyaaas.models.attribute_type import AttributeType
from pyaaas.models.dataset import Dataset
from pyaaas.models import request_builder
import random
import pandas


def dummy_dataset():
    df = pandas.read_csv("scripts/data/dummy-dataset-260219.csv", sep=";")
    dataset = Dataset.from_pandas(df)

    dataset.set_attributes(['Dummy_tag',
                           'Alder',
                           'Sivilstatus',
                           'Barn',
                           'Utdanning'],
                          AttributeType.INSENSITIVE)
    dataset.set_attributes(['ID',
                            'Navn',
                            'Medisinsk forhold'],
                           AttributeType.IDENTIFYING)

    ytelse_hierarchy = pd.read_csv("scripts/data/hierarchies/Ytelse_hierarchy.csv", sep=";", header=None)
    innsatsgruppe_hierarchy = pd.read_csv("scripts/data/hierarchies/innsatsgruppe_hierarchy.csv", sep=";", header=None)
    innvandrerbakgrunn_hierarchy = pd.read_csv("scripts/data/hierarchies/innvandrerbakgrunn_hierarchy.csv", sep=";",
                                               header=None)
    ledighetsstatus_hierarchy = pd.read_csv("scripts/data/hierarchies/ledighetsstatus_hierarchy.csv", sep=";", header=None)
    dataset.set_hierarchy('Ytelse', ytelse_hierarchy)
    dataset.set_hierarchy("Innsatsgruppe", innsatsgruppe_hierarchy)
    dataset.set_hierarchy("Innvandrerbakgrunn", innvandrerbakgrunn_hierarchy)
    dataset.set_hierarchy("Ledighetsstatus", ledighetsstatus_hierarchy)
    return dataset


def dummy_dataset_double_n_times(n):
    df = pandas.read_csv("scripts/data/dummy-dataset-260219.csv", sep=";")
    df = pandas.concat([df] * n)
    dataset = Dataset.from_pandas(df)
    dataset.set_attributes(['Dummy_tag',
                           'Alder',
                           'Sivilstatus',
                           'Barn',
                           'Utdanning'],
                          AttributeType.INSENSITIVE)
    dataset.set_attributes(['ID',
                            'Navn',
                            'Medisinsk forhold'],
                           AttributeType.IDENTIFYING)

    ytelse_hierarchy = pd.read_csv("scripts/data/hierarchies/Ytelse_hierarchy.csv", sep=";", header=None)
    innsatsgruppe_hierarchy = pd.read_csv("scripts/data/hierarchies/innsatsgruppe_hierarchy.csv", sep=";", header=None)
    innvandrerbakgrunn_hierarchy = pd.read_csv("scripts/data/hierarchies/innvandrerbakgrunn_hierarchy.csv", sep=";",
                                               header=None)
    ledighetsstatus_hierarchy = pd.read_csv("scripts/data/hierarchies/ledighetsstatus_hierarchy.csv", sep=";", header=None)
    dataset.set_hierarchy('Ytelse', ytelse_hierarchy)
    dataset.set_hierarchy("Innsatsgruppe", innsatsgruppe_hierarchy)
    dataset.set_hierarchy("Innvandrerbakgrunn", innvandrerbakgrunn_hierarchy)
    dataset.set_hierarchy("Ledighetsstatus", ledighetsstatus_hierarchy)
    return dataset


def generate_dataset(row_num, col_num):
    data = {}
    attributes = {}
    for col in range(col_num):
        index = col % len(column_gen_functions)
        new_column = column_gen_functions[index]

        field_name = new_column[1] + str(new_column[2])
        new_column[2] += 1
        data[field_name] = [new_column[3]() for _ in range(row_num)]
        attributes[field_name] = new_column[0]

    dataframe = pd.DataFrame.from_dict(data)
    headers = dataframe.columns.values.tolist()
    values = dataframe.values.tolist()
    data = [headers] + values
    return Dataset(data, attributes)


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


column_gen_functions = [
    [AttributeType.IDENTIFYING, "name", 0, random_string],
    [AttributeType.QUASIIDENTIFYING, "age", 0, generate_age],
    [AttributeType.QUASIIDENTIFYING, "gender", 0, generate_genders],
    [AttributeType.QUASIIDENTIFYING, "location", 0, generate_location],
]
