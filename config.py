"""Configuration for this server
"""

import os

from server.types import ServerConfig


class Config(ServerConfig):
    """Main Config Gets K, V
         V - From Environment Varaibles By The Name of K
    """
    os.environ["DIRECTORY"] = "./"
    DEBUG = os.environ.get("PROJECT_DEBUG", False) == "True"
