from locust import HttpLocust, TaskSet, task, between

class WebsiteTasks(TaskSet):
        
    @task
    def about(self):
        self.client.get("/api/fibonacci?index=21")

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    wait_time = between(5, 15)