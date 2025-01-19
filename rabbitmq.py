# ============================================================================================================
# Description:  This class integrates with the RabbitMQ messaging broker
#
#
#   03/13/2024 - TOSB-87: AzureKeyVault API --Natalie Carlson
#                           Created
# ============================================================================================================

import pika

from ad_hock.poc.rabbitmq.rabbitmq_processes import RabbitMQProcessA, RabbitMQProcessB


class RabbitMQ:

    def __init__(self, ip_address):

        self.ip_address = ip_address
        self.rabbitmq_object_name_id = f"rmq_{str(id(self))}"

        self.connection = None
        self.channel = None

        # Establish connection
        try:
            # Create connection
            self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.ip_address))
            # Retrieve the channel
            self.channel = self.connection.channel()

            print(f'Established connection {self.rabbitmq_object_name_id} to RabbitMQ {self.ip_address}.')
        except Exception:
            print(f'RabbitMQ connection FAILED for {self.rabbitmq_object_name_id}')
            raise

    def publish_message(self, queue_name, msg):

        # Ensure queue is established
        self.channel.queue_declare(queue=queue_name)

        # Publish message
        self.channel.basic_publish(exchange='', routing_key=queue_name, body=msg)

    def consume_messages(self, queue_name):

        print(f"\tConfirming queue: {queue_name}")

        # Ensure queue is established
        self.channel.queue_declare(queue=queue_name)

        # Publish message
        self.channel.basic_consume(queue=queue_name, auto_ack=True, on_message_callback=eval(f"self.callback_{queue_name}"))

    def close(self):
        """ Closes a connection"""

        if self.connection:
            try:
                self.connection.close()
                print(f'Closed connection {self.rabbitmq_object_name_id} to RabbitMQ {self.ip_address}.')
                self.connection = None
                self.channel = None
            except Exception as e:
                print(f'Failed to close connection {self.rabbitmq_object_name_id} to RabbitMQ {self.ip_address}.')
                print(f'\tError: {str(e)}')

    # ==============================================================
    #   Message Handling Methods
    # ==============================================================

    @staticmethod
    def callback_process_a(ch, method, properties, body):

        print(f"callback: callback_process_a")
        # print(f"\tch: {ch}")
        # print(f"\tmethod: {method}")
        # print(f"\tproperties: {properties}")

        processor = RabbitMQProcessA(body)
        processor.run()

    @staticmethod
    def callback_process_b(ch, method, properties, body):

        print(f"callback: callback_process_b")
        # print(f"\tch: {ch}")
        # print(f"\tmethod: {method}")
        # print(f"\tproperties: {properties}")

        processor = RabbitMQProcessB(body)
        processor.run()
