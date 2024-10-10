import logging
import logging.config
import yaml

def setup_logging(config_path='config/logging.yaml'):
    # Setup logging configuration from a YAML file
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    return logging.getLogger(__name__)