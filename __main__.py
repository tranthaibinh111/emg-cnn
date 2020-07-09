from datetime import datetime
from matplotlib import pyplot as plt
from typing import List

from config import BASE_DIR
from utils import Log
from services import FactoryService, EMGService, PersonService
from models import ActionKind, EMGPosition, PersonModel


# region Private
def __load_uci(folder: str) -> List[PersonModel]:
    """
    Loading physical actions dataset from UCI Machine Learning Repository
    https://archive.ics.uci.edu/ml/datasets/EMG+Physical+Action+Data+Set
    :param folder: download folder
    :return:
    """
    personal: List[PersonModel] = []
    person_service: PersonService = FactoryService.get_instance(PersonService.__name__)

    # Personal 1
    person1 = person_service.load_uci_data(person_name='Person 1', folder_path='{0}/sub1'.format(folder))

    if isinstance(person1, PersonModel):
        personal.append(person1)

    # Personal 2
    person2 = person_service.load_uci_data(person_name='Person 2', folder_path='{0}/sub2'.format(folder))

    if isinstance(person2, PersonModel):
        personal.append(person2)

    # Personal 3
    person3 = person_service.load_uci_data(person_name='Person 3', folder_path='{0}/sub3'.format(folder))

    if isinstance(person3, PersonModel):
        personal.append(person3)

    # Personal 4
    person4 = person_service.load_uci_data(person_name='Person 4', folder_path='{0}/sub4'.format(folder))

    if isinstance(person4, PersonModel):
        personal.append(person4)

    return personal
# end __load_uci()


def __show_plot(personals: List[PersonModel]):
    """
    Show Time Series, Spectrogram, Scalogram from UCI data
    :param personals:
    :return:
    """
    log: Log = Log.get_instance()
    emg_service: EMGService = FactoryService.get_instance(EMGService.__name__)
    person_service: PersonService = FactoryService.get_instance(PersonService.__name__)

    log.debug('Show Plot')

    for personal in personals:
        log.debug('Begin: {0}'.format(personal.name))
        for position in EMGPosition.list():
            # region Normal Physical Actions
            log.debug('{0} - Get Normal Physical Actions'.format(personal.name))
            normal_actions = person_service.get_action(actions=personal.action,
                                                       action_filter=ActionKind.get_normal_action())
            normal_action_names, normal_emg_data = person_service.get_emg(actions=normal_actions, emg_position=position)
            normal_title = 'Normal Physical Actions - {0}'.format(position)
            # Time Series
            log.debug('{0} - Show Time Series - {1}'.format(personal.name, position))
            emg_service.show_time_series(title=normal_title, action_names=normal_action_names, emg_data=normal_emg_data,
                                         low_pass=True, multi_figure=True)
            # Spectrogram
            log.debug('{0} - Show Spectrogram - {1}'.format(personal.name, position))
            emg_service.show_action_spectrogram(title=normal_title, action_names=normal_action_names,
                                                emg_data=normal_emg_data, low_pass=True, multi_figure=True)
            # Scalogram
            log.debug('{0} - Show Scalogram - {1}'.format(personal.name, position))
            emg_service.show_action_scalogram(title=normal_title, action_names=normal_action_names,
                                              emg_data=normal_emg_data, low_pass=True, multi_figure=True)
            # endregion

            # region Aggressive Physical Actions
            log.debug('{0} - Get Aggressive Physical Actions'.format(personal.name))
            aggressive_actions = person_service.get_action(actions=personal.action,
                                                           action_filter=ActionKind.get_aggressive_action())
            aggressive_action_names, aggressive_emg_data = person_service.get_emg(actions=aggressive_actions,
                                                                                  emg_position=position)
            aggressive_title = 'Aggressive Physical Actions - {0}'.format(position)
            # Time Series
            log.debug('{0} - Show Time Series - {1}'.format(personal.name, position))
            emg_service.show_time_series(title=aggressive_title, action_names=aggressive_action_names,
                                         emg_data=aggressive_emg_data, low_pass=False, multi_figure=True)
            # Spectrogram
            log.debug('{0} - Show Spectrogram - {1}'.format(personal.name, position))
            emg_service.show_action_spectrogram(title=aggressive_title, action_names=aggressive_action_names,
                                                emg_data=aggressive_emg_data, low_pass=False, multi_figure=True)
            # Scalogram
            log.debug('{0} - Show Scalogram - {1}'.format(personal.name, position))
            emg_service.show_action_scalogram(title=aggressive_title, action_names=aggressive_action_names,
                                              emg_data=aggressive_emg_data, low_pass=False, multi_figure=True)
            # endregion
        # end for
        log.debug('End: {0}'.format(personal.name))
    # end for
    plt.show()
    log.debug('End Show Plot')

# end __show_plot


def __export_spectrogram(personals: List[PersonModel],
                         source_path: str = '{0}/exports/images/spectrogram/'.format(BASE_DIR)):
    """
    Export Spectrogram image for prepare data (CNN)
    :param personals:
    :param source_path:
    :return:
    """
    log: Log = Log.get_instance()
    emg_service: EMGService = FactoryService.get_instance(EMGService.__name__)

    log.debug('Export Spectrogram Images')
    for personal in personals:
        log.debug('{0}'.format(personal.name))
        for action in personal.action:
            log.debug('{0} : {1}'.format(personal.name, action.name))
            for emg in action.emg_data:
                now = datetime.today()
                file_name = "{0}/{1}-{2}-{3}-{4}.png".format(source_path, action.name, emg.position,
                                                             personal.name, now.strftime("%Y%m%d%H%M%S"))
                log.debug('Saving: {0}'.format(file_name))
                emg_service.export_spectrogram(file_name=file_name, data=emg.data, low_pass=True)
            # end for
            log.debug('End {0} : {1}'.format(personal.name, action.name))
        # end for
        log.debug('End: {0}'.format(personal.name))
    # end for
    log.debug('End Export Spectrogram Images')
# end __export_spectrogram()


def __export_scalogram(personals: List[PersonModel],
                        source_path: str = '{0}/exports/images/scalogram/'.format(BASE_DIR)):
    """
    Export Scalogram image for prepare data (CNN)
    :param personals:
    :param source_path:
    :return:
    """
    log: Log = Log.get_instance()
    emg_service: EMGService = FactoryService.get_instance(EMGService.__name__)

    log.debug('Export Scalogram Images')
    for personal in personals:
        log.debug('{0}'.format(personal.name))
        for action in personal.action:
            log.debug('{0} : {1}'.format(personal.name, action.name))
            for emg in action.emg_data:
                now = datetime.today()
                file_name = "{0}/{1}-{2}-{3}-{4}.png".format(source_path, action.name, emg.position,
                                                             personal.name, now.strftime("%Y%m%d%H%M%S"))
                log.debug('Saving: {0}'.format(file_name))
                emg_service.export_scalogram(file_name=file_name, data=emg.data, low_pass=True)
            # end for
            log.debug('End {0} : {1}'.format(personal.name, action.name))
        # end for
        log.debug('End: {0}'.format(personal.name))
    # end for
    log.debug('End Export Scalogram Images')
# end __export_scalogram()
# endregion


def main():
    personals = __load_uci(folder='{0}/imports/UCI/'.format(BASE_DIR))

    # Show UCI data
    __show_plot(personals)

    # Export Spectrogram Image
    __export_spectrogram(personals)

    # Export Scalogram Image
    __export_scalogram(personals)
# end main()


if __name__ == "__main__":
    main()
