from os import environ

# Set app env
APP_ENV = environ.get('APP_ENV','PROD')

# handle logging
LOGTAIL_TOKEN = environ.get('LOGTAIL_TOKEN','')