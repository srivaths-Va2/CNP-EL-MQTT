import MQTTHandlers

def run_app():
    """
    Run the application by creating an instance of MQTTPublish from MQTTHandlers module and starting the message loop.

    This function initializes an MQTTPublish object and starts the message loop to handle MQTT communication.

    Parameters:
    None

    Returns:
    None
"""
    publish_obj = MQTTHandlers.MQTTPublish()
    publish_obj.start_loop()

if __name__ == "__main__":
    run_app()