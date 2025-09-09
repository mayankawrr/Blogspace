from flask import Flask
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)


print("Package app is loaded")
