# config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    PYTHON_VERSION = os.getenv("PYTHON_VERSION")
    WORKDIR = os.getenv("WORKDIR")
    JAVA_HOME = os.getenv("JAVA_HOME")
    PATH = os.getenv("PATH")

config = Config()
