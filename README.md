## python-app

This project consists of two Python functions: Sender.py and  Receiver.py. The sender function generates the next prime numbers every 5 minutes, publishes them to an MQTT broker and logs the send confirmation, while the receiver function subscribes to the MQTT broker and logs the received prime numbers.

## Prerequisites

Docker and Docker Compose should be installed on your machine.

## Running the application

- Locate to the outer most folder, run the command "docker-compose build" to build the image in docker-compose.yml file.
- When the build is finished, run the command "docker-compose up" to start and run the application.
- You should now see the output of both functions in the terminal.
- OPTIONAL: If you want to run the python app locally in the host machine, you need to change the broker_address variable in both Sender.py and Receiver.py to "127.0.0.1".