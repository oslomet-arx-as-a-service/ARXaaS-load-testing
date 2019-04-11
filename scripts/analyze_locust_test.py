from locust import HttpLocust, TaskSet, task
from scripts.data import test_data
from pyaaas.models.request_builder import RequestBuilder


def analyze_request_content():
    dataset = test_data.dummy_dataset_double_n_times(100)
    request = RequestBuilder(dataset).build_analyze_request()
    return request


request = analyze_request_content()


class UserBehavior(TaskSet):

    @task(1)
    def analyze(self):
        self.client.post("/api/analyze", json=request, verify=False)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 1000
