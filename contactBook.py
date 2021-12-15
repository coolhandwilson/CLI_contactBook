# import necessary modules
import sys
import io


def display_contact_types(sub_books: list):
    """

    :param sub_books:
    :return:
    """
    for number, item in enumerate(sub_books):
        print("Book {:<2}{:*>25}".format(number + 1, sub_books[number]))


def prompt_new_book():
    pass


def prompt_user_options():
    pass


def contact_book(file_name=None):
    """
    Display options for user.

    :return:
    """
    # Allow user to choose main directory file - use default if none provided
    if file_name is None:
        file_name = "master"

    try:
        with open(f"{file_name}.txt", 'r') as master:
            contact_types = master.readlines()
    except FileNotFoundError:
        print("No contact records found.\n")
        contact_types = ''
    else:
        display_contact_types(contact_types)

    if len(contact_types) == 0:
        prompt_new_book()

    else:
        prompt_user_options()
