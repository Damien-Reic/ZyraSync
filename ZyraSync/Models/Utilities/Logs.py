import logging
import os
import yaml
import coloredlogs

class Logs:
    @staticmethod
    def setup_logging(logs_conf_path,logging_level=logging.INFO, env_key='LOG_CFG'):
        value = os.getenv(env_key, None)
        if value:
            logs_conf_path = value
        if os.path.exists(logs_conf_path):
            with open(logs_conf_path, 'rt') as f:
                try:
                    config = yaml.safe_load(f.read())
                    logging.config.dictConfig(config)
                    coloredlogs.install()
                except Exception as e:
                    print(e)
                    print('Error in Logging Configuration. Using default configs')
                    logging.basicConfig(level=logging_level)
                    coloredlogs.install(level=logging_level)
        else:
            logging.basicConfig(level=logging_level)
            coloredlogs.install(level=logging_level)
            print('Failed to load configuration file. Using default configs')

