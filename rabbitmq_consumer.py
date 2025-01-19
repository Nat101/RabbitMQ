import os
import sys
from datetime import datetime
from time import sleep
import RabbitMQ


def main():

    ip_address = 'localhost'  # 'CLNK-DC1-SVRDV1'
    queue_list = [
        'process_a',
        'process_b',
    ]

    # Create instance
    rmq = RabbitMQ(ip_address)

    # Consume messages for queues
    for queue_name in queue_list:

        print(f"Consuming Messages from queue:{queue_name}: {datetime.now()}")
        rmq.consume_messages(queue_name)

    print('Consumer waiting for messages. To exit press CTRL+C')
    rmq.channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Exiting')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
