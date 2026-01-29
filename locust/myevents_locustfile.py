# from locust import HttpUser, task, between

# class MyEventsUser(HttpUser):
#     wait_time = between(1, 2)

#     @task
#     def view_my_events(self):
#         self.client.get("/my-events?user=locust_user")

from locust import HttpUser, task, between

class MyEventsUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def view_my_events(self):
        with self.client.get(
            "/my-events?user=locust_user",
            name="/my-events",
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(f"Status code: {response.status_code}")
            else:
                response.success()