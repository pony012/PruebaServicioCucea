import cf_deployment_tracker
from app.app import app

cf_deployment_tracker.track()

# On Bluemix, get the port number from the environment variable VCAP_APP_PORT
# When running this app on the local machine, default the port to 8080

if __name__ == "__main__":
    app.run(debug = app.config["DEBUG"], host = app.config["HOST"], port = app.config["PORT"])
