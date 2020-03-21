from locust import HttpLocust, TaskSet, task, between

def fibo_example_5(self):
    self.client.get("/api/fibonacci?index=10")
def fibo_example_6(self):
    self.client.get("/api/fibonacci?index=15")
def fibo_example_7(self):
    self.client.get("/api/fibonacci?index=20")
def fibo_example_8(self):
    self.client.get("/api/fibonacci?index=25")
def fibo_example_9(self):
    self.client.get("/api/fibonacci?index=30")
def fibo_example_10(self):
    self.client.get("/api/fibonacci?index=35")
def fibo_example_11(self):
    self.client.get("/api/fibonacci?index=40")
def fibo_example_12(self):
    self.client.get("/api/fibonacci?index=45")
def fibo_example_13(self):
    self.client.get("/api/fibonacci?index=50")
def fibo_example_14(self):
    self.client.get("/api/fibonacci?index=22")
def fibo_example_15(self):
    self.client.get("/api/fibonacci?index=27")
def fibo_example_16(self):
    self.client.get("/api/fibonacci?index=39")
def fibo_example_17(self):
    self.client.get("/api/fibonacci?index=18")
def fibo_example_18(self):
    self.client.get("/api/fibonacci?index=19")
def fibo_example_19(self):
    self.client.get("/api/fibonacci?index=47")
def fibo_example_20(self):
    self.client.get("/api/fibonacci?index=32")
    

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