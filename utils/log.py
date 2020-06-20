import logging
import logging.config
import yaml

from config import *


class Log:
    __instance = None
    __logger = None

    @staticmethod
    def get_instance() -> object:
        """ Static access method. """
        if not Log.__instance:
            Log()
        return Log.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Log.__instance:
            raise Exception("This class is a singleton!")
        else:
            self.__config()
            Log.__instance = self

    def __config(self):
        with open('{0}/config/logging.yaml'.format(BASE_DIR), 'r') as f:
            config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)

        self.__logger = logging.getLogger()

    def debug(self, message: str):
        self.__logger.debug(message)

    def error(self, message: str):
        self.__logger.error(message)
