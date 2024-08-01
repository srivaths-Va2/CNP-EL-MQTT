# MQTT Handlers

This repository contains Python scripts for handling MQTT publish and subscribe methods using the `paho-mqtt` library. The scripts are structured to allow easy implementation of MQTT communication for various applications. Mosquitto is used as the MQTT broker between the publisher and the subscriber. Additionally, Wireshark can be used to analyze the packets transmitted between the publisher and subscriber scripts.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [TLS Setup](#tlssetup)
- [Usage](#usage)

## Description

This project provides two main functionalities:
- **MQTTPublish**: Handles MQTT publishing to a specified topic.
- **MQTTSubscribe**: Handles MQTT subscribing from a specified topic.

The following tools are required in addition to Python3:
- **Mosquitto**: The central MQTT broker, enabling communication between publisher and subscriber.
- **Wireshark**: Used to analyse the network traffic between the publisher and the subscriber.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/srivaths-Va2/CNP-EL-MQTT.git
    cd CNP-EL_MQTT
    ```

2. Install required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Ensure `paho-mqtt` is installed:
    ```sh
    pip install paho-mqtt
    ```

4. Install the mosquitto broker and add it to path. The link to installation can be found here
    [Download](https://mosquitto.org/download/)


5. Install Wireshark. The link to installation can be found here
    [Download](https://www.wireshark.org/download.html)


## TLS Setup

1. For setting up TLS to run the application with encryption, one must install the required certificates for the client and the server. The certificates can be installed using OpenSSL [Download](https://slproweb.com/products/Win32OpenSSL.html). Make sure to add OpenSSL to system path before proceeding forward to downloading certificates. 

2. Open cmd. Type the following commands to create a CA key for the client
    ```sh
    openssl genpkey -algorithm RSA -out client-ca.key
    ```
3. Create a CA certificate using the CA key
    ```sh
    openssl req -new -x509 -key client-ca.key -out client-ca.crt -days 365 -subj "/C=US/ST=State/L=City/O=Organization/OU=Unit/CN=client-ca"
    ```
4. Create a broker key without encryption
    ```sh
    openssl genpkey -algorithm RSA -out broker.key
    ```
5. Request for broker certificate
    ```sh
    openssl req -new -key broker.key -out broker.csr -subj "/C=US/ST=State/L=City/O=Organization/OU=Unit/CN=broker"
    ```
6. Create a broker certificate
    ```sh
    openssl x509 -req -in broker.csr -CA client-ca.crt -CAkey client-ca.key -CA createserial -out broker.crt -days 365
    ```
7. The certificates that are required for us include the `ca.crt`, `server.csr` and `server.key`. Create a new folder under the mosquitto directory called `certs` and save the above three files in there.

8. Also make a copy of the certificate files to store in a folder called `certs` in the local project folder. In config.json, add the paths to the certicates in the `tlsparams` key. 

## Usage

### Running the Project without TLS Encryption

To run the project without TLS encryption

1. Start the Mosquitto broker on cmd-
    ```sh
    mosquitto -v
    ```
    This would initialise the mosquitto broker in verbose mode, and all logs would be displayed on the command line

2. Ensure that the value of `mqtt_port` in `config.json` is set to 1883, the default port for MQTT protocol.

2. Run the subscriber script on python-
    ```sh
    py sub.py run
    ```

3. Run the publisher script on python in another commandline window-
    ```sh
    py pub.py run
    ```

4. After running the publisher, open Wireshark in **Adaptive for Loopback Traffic Capture** mode. Set the filter value to `mqtt` if only the MQTT packets are to be filtered. One may also perform network statistics and throughput computation directly from Wireshark.


### Running the Project with TLS Encryption

To run the project with TLS encryption

1. Update the `mosquitto.conf` file by adding the following lines-
    ```
    listener 8883

    allow_anonymous true
    
    cafile <path to ca.crt>
    keyfile <path to server.key>
    certfile <path to server.crt>

    tls_version tlsv1.2
    ```

2. Start the Mosquitto broker on cmd-
    ```sh
    mosquitto -c "<path to your mosquitto.conf file>" -v
    ```
    This would initialise the mosquitto broker in verbose mode, borrowing the settings added for TLS in the mosquitto.conf file and all logs would be displayed on the command line

3. Ensure that the value of `mqtt_port` in `config.json` is set to 8883, the default port for TLS encryption.

4. Run the subscriber script on python-
    ```sh
    py sub.py run
    ```

5. Run the publisher-TLS script on python in another commandline window-
    ```sh
    py pub_tls.py run
    ```

6. After running the publisher, open Wireshark in **Adaptive for Loopback Traffic Capture** mode. Set the filter value to `tls` if only the TLS packets are to be filtered. One may also perform network statistics and throughput computation directly from Wireshark.
