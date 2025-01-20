# ============================================================================================================
# Description:  This module represents the consumer/server/reciever process.  
#               It establishes a RabbitMQ connection and recieves messages from the producer/client/sender
#
#   01/19/2025 - Natalie Carlson
#                   Created
# ============================================================================================================

# Imports
import os
import sys
from datetime import datetime

from rabbitmq import RabbitMQ


def main():

    # Set IP
    ip_address = 'localhost'
    
    # Create list of queues
    queue_list = [
        'process_a',
        'process_b',
    ]

    # Create instance
    rmq = RabbitMQ(ip_address)

    try:

        # Consume messages from queues
        print(f"Consuming Messages from queues:")
        for queue_name in queue_list:
            print(f"\t{queue_name}")
            rmq.consume_messages(queue_name)

        print('Consumer waiting for messages. To exit press CTRL+C')
        rmq.channel.start_consuming()

    except KeyboardInterrupt:
        # Allow graceful exit
        rmq.close()
        print('Exiting')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

if __name__ == "__main__":
    main()