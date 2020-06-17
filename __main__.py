from config import *
from controllers import *


def main():
    person1 = PersonalController(name="Person 1", folder_path="{0}/EMG/sub1".format(BASE_DIR))
    person2 = PersonalController(name="Person 2", folder_path="{0}/EMG/sub2".format(BASE_DIR))
    person3 = PersonalController(name="Person 3", folder_path="{0}/EMG/sub3".format(BASE_DIR))
    person4 = PersonalController(name="Person 4", folder_path="{0}/EMG/sub4".format(BASE_DIR))


if __name__ == "__main__":
    main()
