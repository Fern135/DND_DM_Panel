from setuptools import setup
from .config import *

CONF = loadConfig()

setup(
    name='FR',
    version=CONF['app']['alpha'],
    py_modules=['cli'],
    install_requires=[
        "click"
    ],
    entry_points={
        'console_scripts': [
                'FR=cli:main',  # yourcli is the command name, cli is the module, main is the function
        ],
    },
)
