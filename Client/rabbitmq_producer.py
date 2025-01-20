# ============================================================================================================
# Description:  This module represents the producer/client/sender process.  
#               It establishes a RabbitMQ connection and sends messages to the consumer/server/reciever
#
#   01/19/2025 - Natalie Carlson
#                   Created
# ============================================================================================================

# Imports
import os
import sys
from datetime import datetime
import random
from time import sleep

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
       
        while True:

            # Randomly pick a queue to simulate random messaging behavior
            queue_name = queue_list[random.randint(0, len(queue_list)-1)]

            # Create msg
            msg = f"queue_name: {queue_name}, timestamp: {datetime.now()}"
            
            # Send message
            print(f"Sending msg:\n\t{msg}")
            rmq.publish_message(queue_name, msg)

            print('Producer sleeping. To exit press CTRL+C')
            sleep(5)
    
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

