# MQTT Handlers

This repository contains Python scripts for handling MQTT publish and subscribe methods using the `paho-mqtt` library. The scripts are structured to allow easy implementation of MQTT communication for various applications. Mosquitto is used as the MQTT broker between the publisher and the subscriber. Additionally, Wireshark can be used to analyze the packets transmitted between the publisher and subscriber scripts.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
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


## Usage

### Running the Publisher

To run the MQTT publisher script:
```sh
py pub.py run
```

### Running the Subscriber

To run the MQTT subscriber script
```sh
py sub.py run
```
