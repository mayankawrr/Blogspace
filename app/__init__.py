from flask import Flask
from .config import Config

app = Flask(__name__)
app.config.from_object(Config) #this loads all env specific config into flask config system
#Flask only loads uppercase attributes from configuration objects or modules because, by convention, uppercase names are used for configuration variables and constants in Python and Flask
#(like SECRET_KEY, DEBUG, SQLALCHEMY_DATABASE_URI) clearly signal that these are intended as configuration settings or constants, not regular variables or helper functions

from app import routes
#app is a package folder
#init is a script which runs everything when package is loaded
#routes, config, forms are modules
#above we import routes module into init 

print("Package app is loaded")
#Forms are not needed during initial boilerplate loading (like in __init__.py), but they will absolutely be imported in other files, such as run.py or route/view modules, whenever a web form is displayed, validated, or processed
