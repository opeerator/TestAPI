from locust import HttpLocust, TaskSet, task, between

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
def fibo_example_11(self):
    self.client.get("/api/fibonacci?index=233")
def fibo_example_12(self):
    self.client.get("/api/fibonacci?index=377")
def fibo_example_13(self):
    self.client.get("/api/fibonacci?index=610")
def fibo_example_14(self):
    self.client.get("/api/fibonacci?index=987")
def fibo_example_15(self):
    self.client.get("/api/fibonacci?index=1597")
def fibo_example_16(self):
    self.client.get("/api/fibonacci?index=2584")
def fibo_example_17(self):
    self.client.get("/api/fibonacci?index=4181")
def fibo_example_18(self):
    self.client.get("/api/fibonacci?index=6765")
def fibo_example_19(self):
    self.client.get("/api/fibonacci?index=10946")
def fibo_example_20(self):
    self.client.get("/api/fibonacci?index=17711")
    

class WebsiteTasks(TaskSet):
    tasks = [
        fibo_example_5,
        fibo_example_6,
        fibo_example_7,
        fibo_example_8,
        fibo_example_9,
        fibo_example_10,
        fibo_example_11,
        fibo_example_12,
        fibo_example_13,
        fibo_example_14,
        fibo_example_15,
        fibo_example_16,
        fibo_example_17,
        fibo_example_18,
        fibo_example_19,
        fibo_example_20
    ]

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    wait_time = between(0, 0)