import os
from dotenv import load_dotenv

load_dotenv()


def get_config_value(key, default=None):
    # Get a configuration value from environment variables
    return os.getenv(key, default)
