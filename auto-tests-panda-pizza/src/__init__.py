# IF YOU DO NOT WANT TO ENCOUNTER THE ModuleNotFind error,
# either list all the modules inside the root package('src' in this case) - STILL DOES NOT WORK WITHOUT SETUP!!!
# OR create the setup.py file according to https://www.youtube.com/watch?v=Mgp6-ZMEcE0

from src.features import environment
from src.features.steps import buy_pizza
from src.features.steps import buy_sushi
