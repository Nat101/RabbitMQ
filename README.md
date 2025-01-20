# RabbitMQ
A demo program of the RabbitMQ Message Broker 

Project dependencies are managed via Pipenv.  See https://pipenv.pypa.io for more information or troubleshooting.ex

# Installation Notes
You need to have the RabbitMQ server installed, please see the installation guide or use the community Docker image.
   
   community Docker image: https://hub.docker.com/_/rabbitmq/
      Note: For my own install I used docker and ran the following build command:
         docker run -d --hostname rabbitmq-server --name rabbitmq-server -p 5672:5672 -p 15672:15672 rabbitmq:4.0-management
         
   installation guide: https://www.rabbitmq.com/docs/download
      You may need to first install Erlang
            If you initially get this error:
               TCP connection succeeded but Erlang distribution failed
               * suggestion: check if the Erlang cookie is identical for all server nodes and CLI tools
                  Note: https://stackoverflow.com/questions/9673172/rabbitmq-erlang-how-to-make-sure-the-erlang-cookies-are-the-same
               * suggestion: check if all server nodes and CLI tools use consistent hostnames when addressing each other
               * suggestion: check if inter-node connections may be configured to use TLS. If so, all nodes and CLI tools must do that
               * suggestion: see the CLI, clustering and networking guides on https://rabbitmq.com/documentation.html to learn more


# Instructions for running program 
This program has two distinct components-
1. The Consumer: This is the "Server" side to which the messages are sent to
2. The Producer: This is the "Client" side to which the messages are sent from

To execute both the Consumer side and the Producer side within a single IDE requires special handling as follows
1. Both the Consumer and Producer run configurations must be set up to allow parallel instances

via PyCharm-
1. Create configurations for rabbitmq_consumer.py/rabbitmq_producer.py 
2. In edit configurations, click on "Modify options"
3. In Modify options select " Allow multiple instances"
4. Note: In the run terminal you can split the views to watch them side by side

via Visual Studio Code
1. Open rabbitmq_consumer.py/rabbitmq_producer.py
2. Navigate to run or debug
3. Click the drop-down
4. Select 'Run in dedicated terminal'
