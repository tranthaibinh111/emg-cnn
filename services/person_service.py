import numpy as np
import os.path

from utils import Log
from models import ActionKind, EMGPosition, ActionModel, EMGModel, PersonalModel


class PersonService:
    def __init__(self):
        self.__log = Log.get_instance()

    # region Private
    def __load_uci_action_data(self, person_name: str, action_name: str, file_path: str) -> ActionModel:
        data = np.loadtxt(open(file_path))
        emg_positions = [EMGPosition.R_Bic, EMGPosition.R_Tri, EMGPosition.L_Bic, EMGPosition.L_Tri,
                         EMGPosition.R_Thi, EMGPosition.R_Ham, EMGPosition.L_Thi, EMGPosition.L_Ham]
        emg_list = [EMGModel(position) for position in emg_positions]
        action = ActionModel(name=action_name, emg_list=emg_list)

        for row in data:
            for index, emg in enumerate(action.emg_list, start=0):
                emg.add_data(row[index])

        # region Show Action Data
        self.__log.debug(message="--------{0} - {1} Action".format(person_name, action_name))

        for emg in action.emg_list:
            self.__log.debug(message="----------------{0}".format(emg.position))
            self.__log.debug('Times (ms): {:d} ms'.format(len(emg.data)))
            self.__log.debug('Amplitude [μV]: {0:d} μV - {1:d} μV'.format(int(min(emg.data)), int(max(emg.data))))
        # endregion
        return action
    # end __load_uci_action_data()
    # endregion

    # region Public
    def load_uci_data(self, person_name: str, folder_path: str, category: str = "txt") -> PersonalModel:
        self.__log.debug(message="{0} - Loading Data".format(person_name))
        data = PersonalModel(name=person_name)

        # region Normal Physical Actions
        self.__log.debug(message="1) Normal Physical Actions")
        normal_actions = [ActionKind.BOWING, ActionKind.CLAPPING, ActionKind.HANDSHAKING, ActionKind.HUGGING,
                          ActionKind.JUMPING, ActionKind.RUNNING, ActionKind.SEATING, ActionKind.STANDING,
                          ActionKind.WALKING, ]

        for action_name in normal_actions:
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
        aggressive_actions = [ActionKind.ELBOWING, ActionKind.FRONTKICKING, ActionKind.HAMERING, ActionKind.HEADERING,
                              ActionKind.KNEEING, ActionKind.PULLING, ActionKind.PUNCHING, ActionKind.PUSHING,
                              ActionKind.SIDEKICKING, ActionKind.SLAPPING]

        for action_name in aggressive_actions:
            file_path = "{0}/Aggressive/{1}/{2}.{1}".format(folder_path, category, action_name)
            if os.path.isfile(file_path):
                action = self.__load_uci_action_data(person_name, action_name, file_path)
                data.add_action(action)
            else:
                self.__log.debug(message="--------{0} Action".format(action))
                self.__log.debug(message="File '{0}' don't exists.".format(file_path))
        # endregion

        self.__log.debug(message="{0} - Loaded Data".format(person_name))
    # end load_uci_data()
    # endregion
