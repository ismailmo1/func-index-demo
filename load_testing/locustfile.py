from random import randint

from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def index(self):
        # create random email to avoid any caching effects
        email = f"{randint(0, 1_000)}@{randint(0, 1_000)}.com"
        data = {
            "email": email,
            "password": "password",
            "submit": "login",
        }
        self.client.post("/login", data=data)
