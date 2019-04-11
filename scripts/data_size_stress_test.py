import timeit
from pyaaas.models.dataset import Dataset
from pyaaas.aaas import AaaS
from pyaaas.models.attribute_type import AttributeType
from pyaaas.models.privacy_models import KAnonymity
import pandas as pd
from scripts.data import test_data
import sys


con = None
dataset = None

def test_dataset(n):
    return test_data.dummy_dataset_double_n_times(n)


def test_window_dataset(row, column):
    return test_data.generate_dataset(row, column)


def anonymize(dataset):
    res = con.anonymize(dataset, [KAnonymity(4)])
    assert res.anonymization_status == "ANONYMOUS"


def analyze(dataset):
    res = con.risk_profile(dataset)
    assert res.re_identification_risk is not None


def dummy_data_anonymize_stress_test(batch_sizes, connector):
    result = {}
    global con
    con = connector
    for batch in batch_sizes:
        elapsed_time = timeit.timeit(f"anonymize(dataset)",
                                     setup=f"dataset = test_dataset({batch})",
                                     globals=globals(),
                                     number=1)
        result[str(batch * 5000)] = elapsed_time
    return result


def dummy_data_analyze_stress_test(batch_sizes, connector):

    global con
    con = connector
    for batch in batch_sizes:
        result = {}
        elapsed_time = timeit.timeit(f"analyze(dataset)",
                                     setup=f"dataset = test_dataset({batch})",
                                     globals=globals(),
                                     number=1)
        result[str(batch * 5000)] = elapsed_time
        yield result


def dataset_window_analyze_stress_test(shapes: list, connector):
    global dataset
    global con
    con = connector

    for shape in shapes:
        result = {}
        dataset = test_window_dataset(shape[0], shape[1])
        size = sys.getsizeof(dataset.to_dataframe().to_csv())
        elapsed_time = timeit.timeit(f"analyze(dataset)",
                                     globals=globals(),
                                     number=1)
        result[str(shape[0])+"x"+str(shape[1])] = (elapsed_time, size)
        yield result

