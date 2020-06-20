from config import *
from services import PersonService, FactoryService


def main():
    person_service: PersonService = FactoryService.get_instance(PersonService.__name__)

    # region Load UCI Machine Learning Repository: EMG Physical Action Data Set Data Set
    person1 = person_service.load_uci_data(person_name="Person 1", folder_path="{0}/EMG/sub1".format(BASE_DIR))
    person2 = person_service.load_uci_data(person_name="Person 2", folder_path="{0}/EMG/sub2".format(BASE_DIR))
    person3 = person_service.load_uci_data(person_name="Person 3", folder_path="{0}/EMG/sub3".format(BASE_DIR))
    person4 = person_service.load_uci_data(person_name="Person 4", folder_path="{0}/EMG/sub4".format(BASE_DIR))
# end main()


if __name__ == "__main__":
    main()
