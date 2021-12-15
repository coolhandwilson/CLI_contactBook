# import necessary modules
import sys
import io




def contact_book():
    """
    Display options for user.

    :return:
    """
    master_file = "master"
    try:
        with open(f"{master_file}.txt", 'r') as master:
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
