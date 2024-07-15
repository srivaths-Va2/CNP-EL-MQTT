# MQTT Handlers

This repository contains Python scripts for handling MQTT publish and subscribe methods using the `paho-mqtt` library. The scripts are structured to allow easy implementation of MQTT communication for various applications.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)

## Description

This project provides two main functionalities:
- **MQTTPublish**: Handles MQTT publishing to a specified topic.
- **MQTTSubscribe**: Handles MQTT subscribing from a specified topic.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/srivaths-Va2/CNP-EL-MQTT.git
    cd CNP-EL_MQTT
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Ensure `paho-mqtt` is installed:
    ```sh
    pip install paho-mqtt
    ```

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
