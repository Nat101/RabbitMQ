import os
import sys
from datetime import datetime
from ad_hock.poc.rabbitmq.rabbitmq import RabbitMQ

import random
from time import sleep


def main():
    ip_address = 'localhost'  # 'CLNK-DC1-SVRDV1'
    queue_list = [
        'process_a',
        'process_b',
    ]

    # Create instance
    rmq = RabbitMQ(ip_address)

    while True:

        # Randomly pick a queue to simulate random messaging behavior
        queue_name = queue_list[random.randint(0, len(queue_list)-1)]

        # Create msg
        msg = f"queue_name: {queue_name}, timestamp: {datetime.now()}"
        print(msg)

        # Send message
        rmq.publish_message(queue_name, msg)

        sleep(5)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Exiting')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
