import MQTTHandlers

def run_app():
    """
    Run the application by creating an instance of MQTTPublish_TLS from MQTTHandlers module and starting the event loop.

    This function initializes an MQTTPublish_TLS object and starts the event loop to publish messages using MQTT protocol.

    Parameters:
    None

    Returns:
    None
    """
    publish_obj = MQTTHandlers.MQTTPublish_TLS()
    publish_obj.start_loop()

if __name__ == "__main__":
    run_app()