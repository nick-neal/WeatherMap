from flask import (
    Flask,
    request,
    url_for,
    render_template
)

import logging
from logtail import LogtailHandler

from settings import (
    APP_ENV,
    LOGTAIL_TOKEN
)
import modules

# Configure logging
handler = LogtailHandler(source_token=LOGTAIL_TOKEN)
logger = logging.getLogger(__name__)
logger.handlers = []
if APP_ENV == "PROD":
    logger.setLevel(logging.INFO)
else:
    logger.setLevel(logging.DEBUG)

logger.addHandler(handler)

# setup flask app
app = Flask(__name__)

@app.route("/")
def index():
    return 'Index Page'

@app.route("/WeatherData")
def weather_data():
    return 'Weather Data'

if __name__ == '__main__':
    if APP_ENV == 'PROD':
        app.run(host='0.0.0.0')
    else:
        app.run(debug=True,host='0.0.0.0')