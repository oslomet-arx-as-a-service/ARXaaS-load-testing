import timeit
from pyaaas.models.dataset import Dataset
from pyaaas.aaas import AaaS
from pyaaas.models.attribute_type import AttributeType
from pyaaas.models.privacy_models import KAnonymity
import pandas as pd
from scripts.data import test_data


con = AaaS("http://localhost:8080")


def test_dataset(n):
    return test_data.dummy_dataset_double_n_times(n)


def anonymize(dataset):
    res = con.anonymize(dataset, [KAnonymity(4)])
    assert res.anonymization_status == "ANONYMOUS"


def analyze(dataset):
    res = con.risk_profile(dataset)
    assert res.re_identification_risk is not None


def dummy_data_anonymize_stress_test(batch_sizes):
    result = {}
    for batch in batch_sizes:
        elapsed_time = timeit.timeit(f"anonymize(dataset)",
                                     setup=f"dataset = test_dataset({batch})",
                                     globals=globals(),
                                     number=1)
        result[str(batch * 5000)] = elapsed_time
    return result


def dummy_data_analyze_stress_test(batch_sizes):
    result = {}
    for batch in batch_sizes:
        elapsed_time = timeit.timeit(f"analyze(dataset)",
                                     setup=f"dataset = test_dataset({batch})",
                                     globals=globals(),
                                     number=1)
        result[str(batch * 5000)] = elapsed_time
    return result
