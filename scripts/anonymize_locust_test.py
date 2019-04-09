from locust import HttpLocust, TaskSet, task
from scripts.data import test_data
from pyaaas.models import request_builder
from pyaaas.models.privacy_models import KAnonymity


def anonymize_request_content():
    kanon = KAnonymity(4)
    dataset = test_data.dummy_dataset_double_n_times(10)
    request = request_builder.RequestBuilder(dataset).add_privacy_model(kanon).build_anonymize_request()
    return request


request = anonymize_request_content()


class UserBehavior(TaskSet):

    @task(1)
    def analyze(self):
        self.client.post("/api/anonymize", json=request)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 1000
