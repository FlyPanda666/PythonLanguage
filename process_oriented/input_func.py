import logging

from utils.common import init_logger
init_logger()
logger = logging.getLogger(__name__)


def whether_ride():
    height = input("How tall are you, in inches ?")
    height = int(height)
    if height >= 36:
        print("\nYou are tall enough to ride !")
    else:
        print("\nYou will be able to ride when you are a little older.")


def get_formatted_name(first_name: str, last_name: str):
    """返回整洁的姓名.
    :param first_name:
    :param last_name:
    :return:
    """
    full_name = first_name + " " + last_name
    return full_name.title()


def format_name():
    while True:
        print("\nPlease tell me your name :")
        print("(enter 'q' at any time to quit!)")
        f_name = input("First name :")
        if f_name == "q":
            break
        l_name = input("Last name :")
        if l_name == "q":
            break
        formatted_name = get_formatted_name(first_name=f_name, last_name=l_name)
        print("\nHello, " + formatted_name + " !")


def climb_mountain():
    responses = {}
    polling_active = True

    while polling_active:
        name = input("\nWhat is your name? ")
        response = input("Which mountain would you like to climb someday? ")
        responses[name] = response

        repeat = input("Would you like to let another person respond? (yes/ no)")

        if repeat == "no":
            polling_active = False

    print("\n--- Poll Result ---")
    for name, response in responses.items():
        print(name + " would like to climb " + response + ".")
