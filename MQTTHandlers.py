# Module to handle MQTT publish and subscribe methods
import paho.mqtt.client as paho
import sys
import time
import logging
import os
from json_parser import JSON_Parser


LOG_DIR = JSON_Parser().get_logging_logdir()
LOG_LVL = getattr(logging, JSON_Parser().get_logging_level().upper())


logging.basicConfig(
    filename=os.path.join(LOG_DIR, JSON_Parser().get_logging_filename()),
    level = LOG_LVL
)

LOGGER = logging.getLogger(__name__)

def onMessage(client, userdata, msg):
    print(msg.topic + ":" + msg.payload.decode())

class MQTTPublish:
    """
    Class to handle MQTT publishing functionality.

    Attributes:
        client: paho.mqtt.client.Client object for MQTT connection.
        port: int, default port for MQTT connection.
        timeout: int, timeout value for MQTT connection.
        host: str, host address for MQTT connection.
        topic: str, topic to publish messages to.
        message: str, message to publish.
        qos: int, quality of service level for message publishing.
        start_time: float, timestamp when the publisher starts running.

    Methods:
        __init__: Constructor method to initialize MQTT client and attributes.
        connect: Method to establish connection with the MQTT broker.
        publish: Method to publish a message to the specified topic.
        run: Method to continuously publish messages until a certain time limit is reached.
        disconnect: Method to disconnect from the MQTT broker.
        start_loop: Method to start the MQTT publishing loop by connecting, publishing, and running the loop.
    """
    def __init__(self) -> None:
        self.client = paho.Client(paho.CallbackAPIVersion.VERSION1)

        self.port = JSON_Parser().get_mqtt_port()
        self.timeout = JSON_Parser().get_mqtt_timeout()
        self.host = JSON_Parser().get_mqtt_host()

        self.topic = JSON_Parser().get_msg_topic()
        self.message = JSON_Parser().get_msg_payload()
        self.qos = JSON_Parser().get_mqtt_qos()

        self.start_time = time.time()


    def connect(self):
        """
        Method to establish connection with the MQTT broker.

        Connects to the MQTT broker using the specified host, port, and timeout values.
        If the connection is successful, prints "Connection to client established!".
        If the connection fails, prints "Could not connect to client!" and exits the program with exit code -1.
        """
        self.client_result = self.client.connect(host=self.host, port=self.port, keepalive=self.timeout)
        if self.client_result != 0:
            # print("Could not connect to client!")
            LOGGER.error("PUB : Could not connect to client!")
            sys.exit(-1)

        elif self.client_result == 0:
            # print("Connection to client established!")
            LOGGER.info("PUB : Connection to client established!")
    
    def publish(self):
        self.client.publish(self.topic, self.message, self.qos)
    
    def run(self):
        """
        Method to continuously publish messages until a certain time limit is reached.

        This method runs a loop that continuously publishes messages to the specified topic with a 5-second interval between each message.
        It checks if the elapsed time since the start of publishing exceeds 200 seconds, and if so, it disconnects the publisher and exits the loop.
        If any exception occurs during the loop, it disconnects from the broker and stops the loop.

        Returns:
            None
        """
        while True:
            try:
                print("Press CTRL+C to exit....")
                LOGGER.debug("PUB : Running the publish loop")
                self.publish()
                LOGGER.debug("PUB : Published message to network")
                time.sleep(5)

                if (time.time() - self.start_time >= 200):
                    # print("Disconnecting the publisher....")
                    LOGGER.warning("PUB : Disconnecting from broker!")
                    self.disconnect()
                    break 
            except:
                # print("Disconnecting from broker!")
                LOGGER.warning("PUB : Disconnecting from broker!")
                self.disconnect()
    
    def disconnect(self):
        """
        Method to disconnect from the MQTT broker.

        Disconnects the client from the MQTT broker by calling the disconnect method of the MQTT client object.
        Logs a message indicating successful disconnection from the network using the LOGGER object.

        Returns:
            None
        """
        self.client.disconnect()
        LOGGER.info("PUB : Disconnected from network!")
    
    def start_loop(self):
        """
        Method to start the MQTT publishing loop by connecting, subscribing, and running the loop.

        This method first establishes a connection with the MQTT broker using the specified host, port, and timeout values.
        Then, it subscribes to the specified topic for receiving messages.
        Finally, it runs a loop that continuously listens for incoming messages until the program is manually terminated.

        Returns:
            None
        """
        self.connect()
        self.run()

class MQTTSubscribe:
    """
    Class to handle MQTT subscribing functionality.

    Attributes:
        client: paho.mqtt.client.Client object for MQTT connection.
        host: str, host address for MQTT connection.
        port: int, default port for MQTT connection.
        timeout: int, timeout value for MQTT connection.
        topic: str, topic to subscribe for receiving messages.
        message: str, message to subscribe for.
        qos: int, quality of service level for message subscribing.

    Methods:
        __init__: Constructor method to initialize MQTT client and attributes.
        connect: Method to establish connection with the MQTT broker.
        subscribe: Method to subscribe to a specific topic for receiving messages.
        run: Method to continuously listen for incoming messages until the program is terminated.
        disconnect: Method to disconnect from the MQTT broker.
        start_loop: Method to start the MQTT subscribing loop by connecting, subscribing, and running the loop.
    """
    def __init__(self) -> None:
        self.client = paho.Client(paho.CallbackAPIVersion.VERSION1)
        self.client.on_message = onMessage

        self.host = JSON_Parser().get_mqtt_host()
        self.port = JSON_Parser().get_mqtt_port()
        self.timeout = JSON_Parser().get_mqtt_timeout()

        self.topic = JSON_Parser().get_msg_topic()
        self.message = JSON_Parser().get_msg_payload()
        self.qos = JSON_Parser().get_mqtt_qos()

    def connect(self):
        """
        Method to establish connection with the MQTT broker.

        Connects to the MQTT broker using the specified host, port, and timeout values.
        If the connection is successful, prints "Connection to client established!".
        If the connection fails, prints "Could not connect to client!" and exits the program with exit code -1.
        """
        self.client_result = self.client.connect(host=self.host, port=self.port, keepalive=self.timeout)
        if self.client_result != 0:
            # print("Could not connect to client!")
            LOGGER.error("SUB : Could not connect to client!")
            sys.exit(-1)
        elif self.client_result == 0:
            # print("Connection to client established!")
            LOGGER.info("SUB : Connection to client established!")
    
    def subscribe(self):
        self.client.subscribe(self.topic)

    def run(self):
        """
        Method to continuously listen for incoming messages until the program is terminated.

        This method initiates a loop that continuously listens for incoming messages from the MQTT broker.
        It prints a message prompting the user to press CTRL+C to exit the loop.
        If an exception occurs during the loop, it prints a message indicating disconnection from the broker and calls the disconnect method to terminate the connection.

        Returns:
            None
        """
        try:
            print("Press CTRL+C to exit....")
            LOGGER.info("SUB : Subscriber waiting for packets")
            self.client.loop_forever()
        except:
            # print("Disconnecting from Broker")
            LOGGER.warning("SUB : Disconnecting from broker!")
            self.disconnect()
    
    def disconnect(self):
        """
        Method to disconnect from the MQTT broker.

        Disconnects the client from the MQTT broker by calling the disconnect method of the MQTT client object.
        Logs a message indicating successful disconnection from the network using the LOGGER object.

        Returns:
            None
        """
        self.client.disconnect()
        LOGGER.info("SUB : Disconnected from network!")
    
    def start_loop(self):
        """
        Method to start the MQTT subscribing loop by connecting, subscribing, and running the loop.

        This method first establishes a connection with the MQTT broker using the specified host, port, and timeout values.
        Then, it subscribes to the specified topic for receiving messages.
        Finally, it runs a loop that continuously listens for incoming messages until the program is manually terminated.

        Returns:
            None
        """
        self.connect()
        self.subscribe()
        self.run()