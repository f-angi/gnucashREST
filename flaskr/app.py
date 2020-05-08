"""
Main module of the server file
"""

import logging

import config
from flask import render_template

# Get the application instance
connex_app = config.connex_app

# Read the swagger.yml file to configure the endpoints
connex_app.add_api("swagger.yml")

logging.basicConfig(filename='logs/app.log', level=logging.DEBUG)
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


# create a URL route in our application for "/"
@connex_app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/
    :return:        the rendered template "home.html"
    """
    return render_template("home.html")


if __name__ == "__main__":
    connex_app.run(host='127.0.0.1', debug=True)
