# ============================================================================================================
# Description:  This class represents a process on the server
#               It is trigger when a message is recieved for queue: process_a
#
#   01/19/2025 - Natalie Carlson
#                   Created
# ============================================================================================================

# Imports
from datetime import datetime


class RabbitMQProcessA:

    def __init__(self, body):

        self.body = body

    def run(self):
        print(f"Running Process: RabbitMQProcessA: {datetime.now()}")
        print(f"\tData: {self.body}")
