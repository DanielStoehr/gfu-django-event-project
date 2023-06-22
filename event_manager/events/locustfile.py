"""
Lasttest mit Locust
locust -f locustfile.py
"""
from locust import HttpUser, between, task

EVENTS_URL = "http://localhost:8000/api/events/"


class EventMangerUser(HttpUser):
    """Lasttest Klasse für Endpunkte der Event-Manager API"""

    wait_time = between(3, 10)

    def on_start(self):
        ...

    @task
    def get_event_overview(self):
        """Lasttest für die Event-Overview"""
        self.client.get(EVENTS_URL)
