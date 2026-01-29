from locust import HttpUser, task, between

# class EventsUser(HttpUser):
#     wait_time = between(1, 2)

#     @task
#     def view_events(self):
#         self.client.get("/events?user=locust_user")



class EventsUser(HttpUser):
    wait_time = between(1, 2)
    USERNAME = "locust_user"

    @task
    def view_events(self):
        with self.client.get(f"/events?user={self.USERNAME}", catch_response=True) as response:
            if response.status_code != 200 or "Events" not in response.text:
                response.failure("Failed to load events page or missing content")