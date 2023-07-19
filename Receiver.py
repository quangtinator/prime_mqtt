import paho.mqtt.client as mqtt
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# MQTT broker settings
broker_address = "mqtt"
broker_port = 1883
topic = "python-app/prime"

# Callback function when a connection is established
def on_connect(client, userdata, flags, rc):
    logger.info("Connected to MQTT broker as receiver with result code: " + str(rc))
    # Subscribe to the topic
    client.subscribe(topic)

# Callback function when a message is received
def on_message(client, userdata, msg):
    prime_number = int(msg.payload)
    logger.info("Received prime number: " + str(prime_number))

# Create an MQTT client instance
client = mqtt.Client()

# Set the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker_address, broker_port, 60)

# Start the MQTT network loop 
client.loop_start()

try:
    while True:
        pass
except KeyboardInterrupt:
    pass

# Disconnect from the broker
client.loop_stop()
client.disconnect()
