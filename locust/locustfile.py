import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    @task
    def test_num_integr(self):
        self.client.get('/numericalintegralservice/0/3.14159')