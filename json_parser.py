# This utility file parses the config-JSON file and returns the config-values

import json
import os

# Globals
JSON_DIR = "C:\\RV-COLLEGE-OF-ENGINEERING\\Sixth Semester\\CNP\\EL\\MQTT_protocol\\code\\config"

class JSON_Parser:
    """
    Class to parse a JSON configuration file for MQTT settings and logging parameters.

    Attributes:
        filename (str): The path to the JSON configuration file.

    Methods:
        get_mqtt_port: Returns the MQTT port specified in the configuration.
        get_mqtt_host: Returns the MQTT host specified in the configuration.
        get_mqtt_timeout: Returns the MQTT timeout specified in the configuration.
        get_mqtt_qos: Returns the MQTT Quality of Service specified in the configuration.
        get_msg_topic: Returns the message topic specified in the configuration.
        get_msg_payload: Returns the message payload specified in the configuration.
        get_logging_logdir: Returns the logging directory specified in the configuration.
        get_logging_filename: Returns the logging filename specified in the configuration.
        get_logging_level: Returns the logging level specified in the configuration.
    """
    def __init__(self) -> None:
        self.filename = os.path.join(JSON_DIR, "config.json")

        with open(self.filename, "r") as jsonfile:
            self.json = json.load(jsonfile)
    
    def get_mqtt_port(self):
        """
        Returns the MQTT port specified in the configuration.

        Returns:
            int: The MQTT port specified in the configuration file.
        """
        return self.json["systemparams"]["mqtt_port"]
    
    def get_mqtt_host(self):
        """
        Returns the MQTT host specified in the configuration.

        Returns:
            str: The MQTT host specified in the configuration file.
        """
        return self.json["systemparams"]["mqtt_host"]
    
    def get_mqtt_timeout(self):
        """
        Returns the MQTT timeout specified in the configuration.

        Returns:
            int: The MQTT timeout specified in the configuration file.
        """
        return self.json["systemparams"]["mqtt_timeout"]
    
    def get_mqtt_qos(self):
        """
        Returns the MQTT Quality of Service specified in the configuration.

        Returns:
            int: The MQTT Quality of Service specified in the configuration file.
        """
        return self.json["systemparams"]["mqtt_qos"]
    
    def get_msg_topic(self):
        """
        Returns the message topic specified in the configuration.

        Returns:
            str: The message topic specified in the configuration file.
        """
        return self.json["messageparams"]["msg_topic"]
    
    def get_msg_payload(self):
        """
        Returns the message payload specified in the configuration.

        Returns:
            str: The message payload specified in the configuration file.
        """
        return self.json["messageparams"]["payload"]
    
    def get_logging_logdir(self):
        """
        Returns the logging directory specified in the configuration.

        Returns:
            str: The logging directory specified in the configuration file.
        """
        return self.json["logging"]["log_dir"]
    
    def get_logging_filename(self):
        """
        Returns the logging filename specified in the configuration.

        Returns:
            str: The logging filename specified in the configuration file.
        """
        return self.json["logging"]["filename"]
    
    def get_logging_level(self):
        """
        Returns the logging level specified in the configuration.

        Returns:
            str: The logging level specified in the configuration file.
        """
        return self.json["logging"]["level"]
    
