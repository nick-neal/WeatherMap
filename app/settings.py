from os import environ

# Set app env
APP_ENV = environ.get('APP_ENV','PROD')

# handle logging
LOGTAIL_TOKEN = environ.get('LOGTAIL_TOKEN','')

# NOAA NWS URL
NOAA_NWS_URL = 'https://api.weather.gov'

# email for contact
CONTACT_EMAIL = environ.get('CONTACT_EMAIL','')