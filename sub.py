import MQTTHandlers

def run_app():
    """
    Run the application by creating an instance of MQTTSubscribe from MQTTHandlers module and starting the event loop.

    Parameters:
        None

    Returns:
        None
    """
    publish_obj = MQTTHandlers.MQTTSubscribe()
    publish_obj.start_loop()

if __name__ == "__main__":
    run_app()