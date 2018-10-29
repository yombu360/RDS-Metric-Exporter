import yaml
import sys
import traceback

from Logger.Logger import Logger


class ConfigParser:
    def __init__(self, config_path):
        self.config_path = config_path

    def _get_config_path(self):
        """Returns path to the config file

        :return: config file path (str)
        """
        return self.config_path

    def parse_config_file(self):
        """Parse the config file and return the content object

        """
        try:
            with open(self.config_path, "r") as config_file:
                config_object = yaml.safe_load(config_file)
            return config_object
        except FileNotFoundError:
            Logger.publish_log_error("Config file not found {}".format(traceback.format_exc()))
            sys.exit(1)
