# DON'T add anything here just add in render's secret or env section 
from os import environ

API_ID = int(environ.get("API_ID", "26468828"))
API_HASH = environ.get("API_HASH", "4693513c08d1ac6af15f95b116c29478")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
