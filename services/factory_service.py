from typing import Dict

from utils import Log
from .person_service import PersonService


class FactoryService:
    __instances: Dict[str, object] = dict()

    @staticmethod
    def get_instance(name: str) -> object:
        """ Static access method """
        if name in FactoryService.__instances:
            return FactoryService.__instances.get(name)

        if name == PersonService.__name__:
            FactoryService.__instances[name] = PersonService()
            return FactoryService.__instances[name]
        else:
            message = "{0} don't exists in FactoryService.__instances".format(name)
            log = Log.get_instance()
            log.error(message)

            return Exception(message)
