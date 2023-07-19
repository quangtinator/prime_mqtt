import paho.mqtt.client as mqtt
import time
import math
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# MQTT broker settings
broker_address = "mqtt"
broker_port = 1883
topic = "python-app/prime"

# Callback function when a connection is established
def on_connect(client, userdata, flags, rc):
    logger.info("Connected to MQTT broker as sender with result code: " + str(rc))

# Create an MQTT client instance
client = mqtt.Client()

# Set the callback function
client.on_connect = on_connect

# Connect to the MQTT broker
client.connect(broker_address, broker_port, 60)

# Start the MQTT network loop 
client.loop_start()

# Check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Find the next prime number
def find_next_prime(num):
    prime = num + 1
    while True:
        if is_prime(prime):
            return prime
        prime += 1

try:
    next_prime = 2
    while True:
        # Publish the next prime number to the topic
        client.publish(topic, str(next_prime))
        logger.info("Sent prime number: " + str(next_prime))
        
        # Calculate the next prime number
        next_prime = find_next_prime(next_prime)
        
        # Wait for 5 minutes
        time.sleep(300)

except KeyboardInterrupt:
    pass

# Disconnect from the broker
client.loop_stop()
client.disconnect()
