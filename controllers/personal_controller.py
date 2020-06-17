import numpy as np
import os.path

from utils import Log
from models import *


class PersonalController:
    def __init__(self, name: str, folder_path: str):
        self.__log = Log.get_instance()
        self.__data = PersonalModel(name)
        self.__load_data(folder_path)

    # region Private
    def __load_action_data(self, action_name: str, file_path: str) -> ActionModel:
        data = np.loadtxt(open(file_path))
        action = ActionModel(name=action_name)

        for row in data:
            # R-Bic: right bicep (C1)
            action.r_bic.add_data(row[0])
            # R-Tri: right tricep (C2)
            action.r_tri.add_data(row[1])
            # L-Bic: left bicep (C3)
            action.l_bic.add_data(row[2])
            # L-Tri: left tricep (C4)
            action.l_tri.add_data(row[3])
            # R-Thi: right thigh (C5)
            action.r_thi.add_data(row[4])
            # R-Ham: right hamstring (C6)
            action.r_ham.add_data(row[5])
            # L-Thi: left thigh (C7)
            action.l_thi.add_data(row[6])
            # L-Ham: left hamstring (C8)
            action.l_ham.add_data(row[7])

        # region Show Action Data
        self.__log.debug(message="--------{0} - {1} Action".format(self.__data.name, action_name))

        # region R-Bic: right bicep (C1)
        emg_data = action.r_bic.data
        self.__log.debug(message="----------------{0}".format("R-Bic: right bicep (C1)"))
        self.__log.debug('Times (ms): {:d} ms'.format(len(emg_data)))
        self.__log.debug('Amplitude [μV]: {0:d} μV - {1:d} μV'.format(int(min(emg_data)), int(max(emg_data))))
        # endregion

        # region R-Tri: right tricep (C2)
        emg_data = action.r_tri.data
        self.__log.debug(message="----------------{0}".format("R-Tri: right tricep (C2)"))
        self.__log.debug('Times (ms): {:d} ms'.format(len(emg_data)))
        self.__log.debug('Amplitude [μV]: {0:d} μV - {1:d} μV'.format(int(min(emg_data)), int(max(emg_data))))
        # endregion

        # region L-Bic: left bicep (C3)
        emg_data = action.l_bic.data
        self.__log.debug(message="----------------{0}".format("L-Bic: left bicep (C3)"))
        self.__log.debug('Times (ms): {:d} ms'.format(len(emg_data)))
        self.__log.debug('Amplitude [μV]: {0:d} μV - {1:d} μV'.format(int(min(emg_data)), int(max(emg_data))))
        # endregion

        # region L-Tri: left tricep (C4)
        emg_data = action.l_tri.data
        self.__log.debug(message="----------------{0}".format("L-Tri: left tricep (C4)"))
        self.__log.debug('Times (ms): {:d} ms'.format(len(emg_data)))
        self.__log.debug('Amplitude [μV]: {0:d} μV - {1:d} μV'.format(int(min(emg_data)), int(max(emg_data))))
        # endregion

        # region R-Thi: right thigh (C5)
        emg_data = action.r_thi.data
        self.__log.debug(message="----------------{0}".format("R-Thi: right thigh (C5)"))
        self.__log.debug('Times (ms): {:d} ms'.format(len(emg_data)))
        self.__log.debug('Amplitude [μV]: {0:d} μV - {1:d} μV'.format(int(min(emg_data)), int(max(emg_data))))
        # endregion

        # region R-Ham: right hamstring (C6)
        emg_data = action.r_ham.data
        self.__log.debug(message="----------------{0}".format("R-Ham: right hamstring (C6)"))
        self.__log.debug('Times (ms): {:d} ms'.format(len(emg_data)))
        self.__log.debug('Amplitude [μV]: {0:d} μV - {1:d} μV'.format(int(min(emg_data)), int(max(emg_data))))
        # endregion

        # region L-Thi: left thigh (C7)
        emg_data = action.l_thi.data
        self.__log.debug(message="----------------{0}".format("L-Thi: left thigh (C7)"))
        self.__log.debug('Times (ms): {:d} ms'.format(len(emg_data)))
        self.__log.debug('Amplitude [μV]: {0:d} μV - {1:d} μV'.format(int(min(emg_data)), int(max(emg_data))))
        # endregion

        # region L-Ham: left hamstring (C8)
        emg_data = action.l_ham.data
        self.__log.debug(message="----------------{0}".format("L-Ham: left hamstring (C8)"))
        self.__log.debug('Times (ms): {:d} ms'.format(len(emg_data)))
        self.__log.debug('Amplitude [μV]: {0:d} μV - {1:d} μV'.format(int(min(emg_data)), int(max(emg_data))))
        # endregion
        # endregion
        return action

    def __load_data(self, folder_path: str, category: str = "txt"):
        self.__log.debug(message="{0} - Loading Data".format(self.__data.name))

        # region Normal Physical Actions
        self.__log.debug(message="1) Normal Physical Actions")

        # region Bowing Actions
        file_path = "{0}/Normal/{1}/{2}.{1}".format(folder_path, category, ActionKind.BOWING)
        if os.path.isfile(file_path):
            self.__data.bowing = self.__load_action_data(ActionKind.BOWING, file_path)
        else:
            self.__log.debug(message="--------{0} Action".format(ActionKind.BOWING))
            self.__log.debug(message="File '{0}' don't exists.".format(file_path))
        # endregion

        # region Clapping Actions
        file_path = "{0}/Normal/{1}/{2}.{1}".format(folder_path, category, ActionKind.CLAPPING)
        if os.path.isfile(file_path):
            self.__data.clapping = self.__load_action_data(ActionKind.CLAPPING, file_path)
        else:
            self.__log.debug(message="--------{0} Action".format(ActionKind.CLAPPING))
            self.__log.debug(message="File '{0}' don't exists.".format(file_path))
        # endregion

        # region Handshaking Actions
        file_path = "{0}/Normal/{1}/{2}.{1}".format(folder_path, category, ActionKind.HANDSHAKING)
        if os.path.isfile(file_path):
            self.__data.hamering = self.__load_action_data(ActionKind.HANDSHAKING, file_path)
        else:
            self.__log.debug(message="--------{0} Action".format(ActionKind.HANDSHAKING))
            self.__log.debug(message="File '{0}' don't exists.".format(file_path))
        # endregion

        # region Hugging Actions
        file_path = "{0}/Normal/{1}/{2}.{1}".format(folder_path, category, ActionKind.HUGGING)
        if os.path.isfile(file_path):
            self.__data.hugging = self.__load_action_data(ActionKind.HUGGING, file_path)
        else:
            self.__log.debug(message="--------{0} Action".format(ActionKind.HUGGING))
            self.__log.debug(message="File '{0}' don't exists.".format(file_path))
        # endregion

        # region Jumping Actions
        file_path = "{0}/Normal/{1}/{2}.{1}".format(folder_path, category, ActionKind.JUMPING)
        if os.path.isfile(file_path):
            self.__data.jumping = self.__load_action_data(ActionKind.JUMPING, file_path)
        else:
            self.__log.debug(message="--------{0} Action".format(ActionKind.JUMPING))
            self.__log.debug(message="File '{0}' don't exists.".format(file_path))
        # endregion

        # region Running Actions
        file_path = "{0}/Normal/{1}/{2}.{1}".format(folder_path, category, ActionKind.RUNNING)
        if os.path.isfile(file_path):
            self.__data.running = self.__load_action_data(ActionKind.RUNNING, file_path)
        else:
            self.__log.debug(message="--------{0} Action".format(ActionKind.RUNNING))
            self.__log.debug(message="File '{0}' don't exists.".format(file_path))
        # endregion

        # region Seating Actions
        file_path = "{0}/Normal/{1}/{2}.{1}".format(folder_path, category, ActionKind.SEATING)
        if os.path.isfile(file_path):
            self.__data.seating = self.__load_action_data(ActionKind.SEATING, file_path)
        else:
            self.__log.debug(message="--------{0} Action".format(ActionKind.SEATING))
            self.__log.debug(message="File '{0}' don't exists.".format(file_path))
        # endregion

        # region Standing Actions
        file_path = "{0}/Normal/{1}/{2}.{1}".format(folder_path, category, ActionKind.STANDING)
        if os.path.isfile(file_path):
            self.__data.standing = self.__load_action_data(ActionKind.STANDING, file_path)
        else:
            self.__log.debug(message="--------{0} Action".format(ActionKind.STANDING))
            self.__log.debug(message="File '{0}' don't exists.".format(file_path))
        # endregion

        # region Walking Actions
        file_path = "{0}/Normal/{1}/{2}.{1}".format(folder_path, category, ActionKind.WALKING)
        if os.path.isfile(file_path):
            self.__data.walking = self.__load_action_data(ActionKind.WALKING, file_path)
        else:
            self.__log.debug(message="--------{0} Action".format(ActionKind.WALKING))
            self.__log.debug(message="File '{0}' don't exists.".format(file_path))
        # endregion

        # region Waving Actions
        file_path = "{0}/Normal/{1}/{2}.{1}".format(folder_path, category, ActionKind.WAVING)
        if os.path.isfile(file_path):
            self.__data.waving = self.__load_action_data(ActionKind.WAVING, file_path)
        else:
            self.__log.debug(message="--------{0} Action".format(ActionKind.WAVING))
            self.__log.debug(message="File '{0}' don't exists.".format(file_path))
        # endregion
        # endregion

        # region Aggressive Physical Actions
        self.__log.debug(message="2) Aggressive Physical Actions")

        # region Elbowing Actions
        file_path = "{0}/Aggressive/{1}/{2}.{1}".format(folder_path, category, ActionKind.ELBOWING)
        if os.path.isfile(file_path):
            self.__data.elbowing = self.__load_action_data(ActionKind.ELBOWING, file_path)
        else:
            self.__log.debug(message="--------{0} Action".format(ActionKind.ELBOWING))
            self.__log.debug(message="File '{0}' don't exists.".format(file_path))
        # endregion

        # region Frontkicking Actions
        file_path = "{0}/Aggressive/{1}/{2}.{1}".format(folder_path, category, ActionKind.FRONTKICKING)
        if os.path.isfile(file_path):
            self.__data.frontkicking = self.__load_action_data(ActionKind.FRONTKICKING, file_path)
        else:
            self.__log.debug(message="--------{0} Action".format(ActionKind.FRONTKICKING))
            self.__log.debug(message="File '{0}' don't exists.".format(file_path))
        # endregion

        # region Hamering Actions
        file_path = "{0}/Aggressive/{1}/{2}.{1}".format(folder_path, category, ActionKind.HAMERING)
        if os.path.isfile(file_path):
            self.__data.hamering = self.__load_action_data(ActionKind.HAMERING, file_path)
        else:
            self.__log.debug(message="--------{0} Action".format(ActionKind.HAMERING))
            self.__log.debug(message="File '{0}' don't exists.".format(file_path))
        # endregion

        # region Headering Actions
        file_path = "{0}/Aggressive/{1}/{2}.{1}".format(folder_path, category, ActionKind.HEADERING)
        if os.path.isfile(file_path):
            self.__data.headering = self.__load_action_data(ActionKind.HEADERING, file_path)
        else:
            self.__log.debug(message="--------{0} Action".format(ActionKind.HEADERING))
            self.__log.debug(message="File '{0}' don't exists.".format(file_path))
        # endregion

        # region Kneeing Actions
        file_path = "{0}/Aggressive/{1}/{2}.{1}".format(folder_path, category, ActionKind.KNEEING)
        if os.path.isfile(file_path):
            self.__data.kneeing = self.__load_action_data(ActionKind.KNEEING, file_path)
        else:
            self.__log.debug(message="--------{0} Action".format(ActionKind.KNEEING))
            self.__log.debug(message="File '{0}' don't exists.".format(file_path))
        # endregion

        # region Pulling Actions
        file_path = "{0}/Aggressive/{1}/{2}.{1}".format(folder_path, category, ActionKind.PULLING)
        if os.path.isfile(file_path):
            self.__data.pulling = self.__load_action_data(ActionKind.PULLING, file_path)
        else:
            self.__log.debug(message="--------{0} Action".format(ActionKind.PULLING))
            self.__log.debug(message="File '{0}' don't exists.".format(file_path))
        # endregion

        # region Punching Actions
        file_path = "{0}/Aggressive/{1}/{2}.{1}".format(folder_path, category, ActionKind.PUNCHING)
        if os.path.isfile(file_path):
            self.__data.punching = self.__load_action_data(ActionKind.PUNCHING, file_path)
        else:
            self.__log.debug(message="--------{0} Action".format(ActionKind.PUNCHING))
            self.__log.debug(message="File '{0}' don't exists.".format(file_path))
        # endregion

        # region Pushing Actions
        file_path = "{0}/Aggressive/{1}/{2}.{1}".format(folder_path, category, ActionKind.PUSHING)
        if os.path.isfile(file_path):
            self.__data.pushing = self.__load_action_data(ActionKind.PUSHING, file_path)
        else:
            self.__log.debug(message="--------{0} Action".format(ActionKind.PUSHING))
            self.__log.debug(message="File '{0}' don't exists.".format(file_path))
        # endregion

        # region Sidekicking Actions
        file_path = "{0}/Aggressive/{1}/{2}.{1}".format(folder_path, category, ActionKind.SIDEKICKING)
        if os.path.isfile(file_path):
            self.__data.sidekicking = self.__load_action_data(ActionKind.SIDEKICKING, file_path)
        else:
            self.__log.debug(message="--------{0} Action".format(ActionKind.SIDEKICKING))
            self.__log.debug(message="File '{0}' don't exists.".format(file_path))
        # endregion

        # region Slapping Actions
        file_path = "{0}/Aggressive/{1}/{2}.{1}".format(folder_path, category, ActionKind.SLAPPING)
        if os.path.isfile(file_path):
            self.__data.slapping = self.__load_action_data(ActionKind.SLAPPING, file_path)
        else:
            self.__log.debug(message="--------{0} Action".format(ActionKind.SLAPPING))
            self.__log.debug(message="File '{0}' don't exists.".format(file_path))
        # endregion
        # endregion

        self.__log.debug(message="{0} - Loaded Data".format(self.__data.name))
    # endregion

    # region Publish
    @property
    def data(self) -> PersonalModel:
        return self.__data
    # endregion
