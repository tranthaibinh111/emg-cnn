from matplotlib import pyplot as plt

from config import *
from services import FactoryService, EMGService, PersonService
from models import ActionKind, EMGPosition


def main():
    emg_service: EMGService = FactoryService.get_instance(EMGService.__name__)
    person_service: PersonService = FactoryService.get_instance(PersonService.__name__)

    # region Load UCI Machine Learning Repository: EMG Physical Action Data Set Data Set
    person1 = person_service.load_uci_data(person_name="Person 1", folder_path="{0}/EMG/sub1".format(BASE_DIR))
    # person2 = person_service.load_uci_data(person_name="Person 2", folder_path="{0}/EMG/sub2".format(BASE_DIR))
    # person3 = person_service.load_uci_data(person_name="Person 3", folder_path="{0}/EMG/sub3".format(BASE_DIR))
    # person4 = person_service.load_uci_data(person_name="Person 4", folder_path="{0}/EMG/sub4".format(BASE_DIR))
    # endregion

    # region Show plot
    normal_actions = person_service.get_action(actions=person1.action,
                                               action_filter=ActionKind.get_normal_action())
    action_names, emg_data = person_service.get_emg(actions=normal_actions, emg_position=EMGPosition.R_Bic)

    emg_service.show_action(title="Normal Physical Actions", action_names=action_names, emg_data=emg_data,
                            low_pass=True, multi_figure=True)
    emg_service.show_action_spectrogram(title="Normal Physical Actions", action_names=action_names, emg_data=emg_data,
                                        low_pass=True, multi_figure=True)
    # aggressive_actions = person_service.get_action(actions=person1.action,
    #                                                action_filter=ActionKind.get_aggressive_action())
    # emg_service.show_action(action_name="Aggressive Physical Actions",
    #                         actions=aggressive_actions,
    #                         emg_position=EMGPosition.R_Bic,
    #                         multi_figure=True)
    plt.show()
    # endregion
# end main()


if __name__ == "__main__":
    main()
