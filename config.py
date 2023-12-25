import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("", ""))
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("", "")
LOG_CHANNEL = int(environ.get("-1002046525344", ""))
ADMINS = int(environ.get("1410065122", ""))
DB_URI = environ.get("DB_URI", "mongodb+srv://sushankm16:4i1WAfPYKWyqPIDD@cluster0.sngp9pz.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "sushankm16")
OPENAI_API = environ.get("OPENAI_API", "sk-msym9N9zmWvNABnaRUo1T3B1bkF Jjkn8Y1nvEYgM1kr5yIqg")
AI = is_enabled((environ.get("AI","True")), False)
