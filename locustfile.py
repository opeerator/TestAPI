from locust import HttpLocust, TaskSet, task, between

def fibo_example_1(self):
    self.client.get("/api/fibonacci?index=0")
def fibo_example_2(self):
    self.client.get("/api/fibonacci?index=1")
def fibo_example_3(self):
    self.client.get("/api/fibonacci?index=5")
def fibo_example_4(self):
    self.client.get("/api/fibonacci?index=8")
def fibo_example_5(self):
    self.client.get("/api/fibonacci?index=13")
def fibo_example_6(self):
    self.client.get("/api/fibonacci?index=21")
def fibo_example_7(self):
    self.client.get("/api/fibonacci?index=34")
def fibo_example_8(self):
    self.client.get("/api/fibonacci?index=55")
def fibo_example_9(self):
    self.client.get("/api/fibonacci?index=89")
def fibo_example_10(self):
    self.client.get("/api/fibonacci?index=144")
    

class WebsiteTasks(TaskSet):
    tasks = [
        fibo_example_1,
        fibo_example_2,
        fibo_example_3,
        fibo_example_4,
        fibo_example_5,
        fibo_example_6,
        fibo_example_7,
        fibo_example_8,
        fibo_example_9,
        fibo_example_10
    ]

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    wait_time = between(0, 0)