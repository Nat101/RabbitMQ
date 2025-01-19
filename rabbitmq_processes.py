
from datetime import datetime


class RabbitMQProcessA:

    def __init__(self, body):

        self.body = body

    def run(self):
        print(f"\tRunning Process: RabbitMQProcessA: {datetime.now()}")
        print(f"\t\t{self.body}")


class RabbitMQProcessB:

    def __init__(self, body):

        self.body = body

    def run(self):
        print(f"\tRunning Process: RabbitMQProcessB: {datetime.now()}")
        print(f"\t\t{self.body}")
