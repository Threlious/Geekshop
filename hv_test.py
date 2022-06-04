from locust import HttpUser, TaskSet, task


def index(l):
    l.client.get("/")


def products(l):
    l.client.get("/products/")


# def login(l):
#     l.client.post("/auth/login/", {"username": "", "password": ""})
#
#
# def logout(l):
#     l.client.post("/auth/logout/", {"username": "", "password": ""})


@task
class UserBehavior(TaskSet):
    tasks = {index: 2, products: 5}

    # def on_start(self):
    #     login(self)
    #
    # def on_stop(self):
    #     logout(self)


@task
class WebsiteUser(HttpUser):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000

# locust -f hv_test.py --host=http://localhost:8000
