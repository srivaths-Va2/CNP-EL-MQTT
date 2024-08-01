# This utility file parses the config-JSON file and returns the config-values

import json
import os

# Globals
JSON_DIR = "C:\\RV-COLLEGE-OF-ENGINEERING\\Sixth Semester\\CNP\\EL\\MQTT_protocol\\CNP-EL-MQTT\\config"

class JSON_Parser:
    """Class for parsing a JSON configuration file and retrieving specific parameters.

    Attributes:
        filename (str): The path to the JSON configuration file.
        json (dict): The parsed JSON content.

    Methods:
        get_mqtt_port: Retrieve the MQTT port from the configuration.
        get_mqtt_host: Retrieve the MQTT host from the configuration.
        get_mqtt_timeout: Retrieve the MQTT timeout from the configuration.
        get_mqtt_qos: Retrieve the MQTT quality of service from the configuration.
        get_msg_topic: Retrieve the message topic from the configuration.
        get_msg_payload: Retrieve the message payload from the configuration.
        get_logging_logdir: Retrieve the logging directory from the configuration.
        get_logging_filename: Retrieve the logging filename from the configuration.
        get_logging_level: Retrieve the logging level from the configuration.
        get_tlsparams_cacerts: Retrieve the CA certificates path for TLS from the configuration.
        get_tlsparams_certfile: Retrieve the certificate file path for TLS from the configuration.
        get_tlsparams_keyfile: Retrieve the key file path for TLS from the configuration.
    """
    def __init__(self) -> None:
        self.filename = os.path.join(JSON_DIR, "config.json")

        with open(self.filename, "r") as jsonfile:
            self.json = json.load(jsonfile)
    
    def get_mqtt_port(self):
        return self.json["systemparams"]["mqtt_port"]
    
    def get_mqtt_host(self):
        return self.json["systemparams"]["mqtt_host"]
    
    def get_mqtt_timeout(self):
        return self.json["systemparams"]["mqtt_timeout"]
    
    def get_mqtt_qos(self):
        return self.json["systemparams"]["mqtt_qos"]
    
    def get_msg_topic(self):
        return self.json["messageparams"]["msg_topic"]
    
    def get_msg_payload(self):
        return self.json["messageparams"]["payload"]
    
    def get_logging_logdir(self):
        return self.json["logging"]["log_dir"]
    
    def get_logging_filename(self):
        return self.json["logging"]["filename"]
    
    def get_logging_level(self):
        return self.json["logging"]["level"]
    
    def get_tlsparams_cacerts(self):
        return self.json["tlsparams"]["ca_certs"]
    
    def get_tlsparams_certfile(self):
        return self.json["tlsparams"]["certfile"]
    
    def get_tlsparams_keyfile(self):
        return self.json["tlsparams"]["keyfile"]
    
