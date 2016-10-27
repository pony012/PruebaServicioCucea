import cf_deployment_tracker
import os
from app.app import app

cf_deployment_tracker.track()

# On Bluemix, get the port number from the environment variable VCAP_APP_PORT
# When running this app on the local machine, default the port to 8080
port = int(os.getenv('VCAP_APP_PORT', 8080))

host = str(os.getenv('VCAP_APP_HOST', "127.0.0.1"))

debug = True if port == 8080 else False

if __name__ == "__main__":
    app.run(debug = debug, host = host, port = port)
