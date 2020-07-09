import numpy as np
import os.path

from typing import List, Tuple

from utils import Log
from models import ActionKind, EMGPosition, ActionModel, EMGModel, PersonModel


class PersonService:
    def __init__(self):
        self.__log = Log.get_instance()

    # region Private
    def __load_uci_action_data(self, person_name: str, action_name: str, file_path: str) -> ActionModel:
        data = np.loadtxt(open(file_path))
        emg_positions = [EMGPosition.R_BIC, EMGPosition.R_TRI, EMGPosition.L_BIC, EMGPosition.L_TRI,
                         EMGPosition.R_THI, EMGPosition.R_HAM, EMGPosition.L_THI, EMGPosition.L_HAM]
        emg_data = [EMGModel(position) for position in emg_positions]
        action = ActionModel(name=action_name, emg_data=emg_data)

        for row in data:
            for index, emg in enumerate(action.emg_data, start=0):
                emg.add_data(row[index])

        # region Show Action Data
        self.__log.debug(message="--------{0} - {1} Action".format(person_name, action_name))

        for emg in action.emg_data:
            self.__log.debug(message="----------------{0}".format(emg.position))
            self.__log.debug('Times (ms): {:d} ms'.format(len(emg.data)))
            self.__log.debug('Amplitude [μV]: {0:d} μV - {1:d} μV'.format(int(min(emg.data)), int(max(emg.data))))
        # endregion
        return action
    # end __load_uci_action_data()
    # endregion

    # region Public
    def load_uci_data(self, person_name: str, folder_path: str, category: str = "txt") -> PersonModel:
        self.__log.debug(message="{0} - Loading Data".format(person_name))
        data = PersonModel(name=person_name)

        # region Normal Physical Actions
        self.__log.debug(message="1) Normal Physical Actions")

        for action_name in ActionKind.get_normal_action():
            file_path = "{0}/Normal/{1}/{2}.{1}".format(folder_path, category, action_name)
            if os.path.isfile(file_path):
                action = self.__load_uci_action_data(person_name, action_name, file_path)
                data.add_action(action)
            else:
                self.__log.debug(message="--------{0} Action".format(action_name))
                self.__log.debug(message="File '{0}' don't exists.".format(file_path))
        # endregion

        # region Aggressive Physical Actions
        self.__log.debug(message="2) Aggressive Physical Actions")

        for action_name in ActionKind.get_aggressive_action():
            file_path = "{0}/Aggressive/{1}/{2}.{1}".format(folder_path, category, action_name)
            if os.path.isfile(file_path):
                action = self.__load_uci_action_data(person_name, action_name, file_path)
                data.add_action(action)
            else:
                self.__log.debug(message="--------{0} Action".format(action))
                self.__log.debug(message="File '{0}' don't exists.".format(file_path))
        # endregion

        self.__log.debug(message="{0} - Loaded Data".format(person_name))
        return data
    # end load_uci_data()

    # noinspection PyMethodMayBeStatic
    def get_action(self, actions: List[ActionModel], action_filter: List[str]) -> List[ActionModel]:
        result: List[ActionModel] = list()

        # check person
        if actions is None or len(actions) == 0:
            self.__log.error(message="The actions parameter was none or empty in the get_action function")
            return result

        # check action_filter
        if action_filter is None or len(action_filter) == 0:
            self.__log.error(message="The action_filter parameter was none or empty in the get_action function")
            return result

        for item in actions:
            if item.name in action_filter:
                result.append(item)

        return result
    # end get_action()

    # noinspection PyMethodMayBeStatic
    def get_emg(self, actions: List[ActionModel], emg_position: str) -> Tuple[List[str], List[List[float]]]:
        names: List[str] = list()
        emg_data: List[List[float]] = list()

        # check actions
        if actions is None or len(actions) == 0:
            self.__log.error(message="The actions parameter was none or empty in the get_action function")
            return names, emg_data

        # check emg_position
        if not emg_position:
            self.__log.error(message="The emg_position parameter was none or empty in the get_action function")
            return names, emg_data

        for action in actions:
            for emg in action.emg_data:
                if emg.position == emg_position:
                    names.append(action.name)
                    emg_data.append(emg.data)

        return names, emg_data
    # end get_emg()
    # endregion
# end class PersonService
