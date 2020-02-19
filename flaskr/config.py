import os

import connexion
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

# Create the Connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)
# Get the underlying Flask app instance
app = connex_app.app

# Initialize Marshmallow
ma = Marshmallow(app)
