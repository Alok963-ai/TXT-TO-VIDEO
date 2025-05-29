# DON'T add anything here just add in render's secret or env section 
from os import environ

API_ID = int(environ.get("API_ID", "26572696"))
API_HASH = environ.get("API_HASH", "67a8947a3e1b15f9ef9684286baa34cb")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
