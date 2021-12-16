# import necessary modules
import sys
import json
import io


def display_contact_types(sub_books: list):
    """
    Display sub-books in enumerated list.

    :param sub_books: a list
    :pre-condition: sub_books must be a list of contact sub-books present in the user's central directory
    :post-condition: no change to arguments submitted to this function
    :return: None
    """
    for number, item in enumerate(sub_books):
        print("Book {:<2}{:*>25}".format(number + 1, sub_books[number]))


def new_sublist(current_file: list):
    """
    Add new sub-book to the central directory, create associated JSON file.

    :param current_file: a list
    :pre-condition: current_file must be a list of the current sub-books in the central directory
    :post-condition: no changes to current_file; user selection stored in local variable and returned
    :return: the user's selection for a new sub-book of contacts
    """
    categories = ['Friends', 'Business', 'School', 'Family']

    # Remove pre-existing address books from user options
    if current_file != 0:
        for item in categories.copy():
            if item in current_file:
                categories.remove(item)

    # Get user choice of new address book
    while True:
        print("Please choose a new sub-category: \n")
        display_contact_types(categories)
        choice = input("Please enter the corresponding number of the category you wish to create.\n")

        if choice not in [str(number) for number in range(1, len(categories) + 1)]:
            print("Invalid input. Please enter numeric values only.\n")

        else:
            choice = int(choice)
            print(f"Wonderful. You have selected {categories[choice - 1]}.")
            return categories[choice - 1]


def create_new_file(new_file_name: str, file_type: bool = False, central: str = "central"):
    """
    Create a new json or txt file.

    :param new_file_name: a string
    :param file_type: a boolean
    :param central: a string or None
    :pre-condition: new_file_name must be a string representing the name of the new file to be created
    :pre-condition: file_type must be True if the new file is to be a text file, False if it is to be a json file
    :pre-condition: central will store the name of the new central directory file to be created, if any
    :post-condition: a new file, json or txt, is created in the working directory
    :return: None
    """
    category_type = 'json'

    # If True, then we are creating the central directory (a text file)
    if file_type is True:
        category_type = 'txt'

    with open(f"{new_file_name}.{category_type}", 'w') as new_file:
        new_file.write("")

    # If this is a sub-file, add it to our central directory
    if file_type is False:
        with open(f"{central}.txt", 'a+') as central:
            central.write(f"{new_file_name}\n")

        print("New sub-file created!\n")


def prompt_new_book(contact_sublist: list):
    """
    Get user's choice for new sub-book of contacts.

    :param contact_sublist: a list
    :pre-condition: contact_sublist must be a list of the current, active contact sub-books in the central directory
    :post-condition: a new sub-book file is created, added to the central directory
    :return: None
    """
    # If no other books exist
    if len(contact_sublist) == 0:
        print("Hello! you don't seem to have any entries in your address book. Let's start with making a new category.")

    user_choice = new_sublist(contact_sublist)

    # Create new file with chosen category name
    create_new_file(user_choice)

    # Add file to central directory

    # Provide the user with their options for adding, revising, viewing their contacts
    prompt_user_options(contact_sublist)


def add_contact(address_book: str):
    """
    Add a contact entry to a sub-book.

    :param address_book: a string
    :pre-condition: address_book must be the name of the sub-book that the entry is to be added to
    :post-condition: new contact json object is added to the address sub-book
    :return: None
    """
    entry = {
        "Name": input("Please enter your contact's name... \n"),
        "Number": input("Please enter their number... \n"),
        "Address": input("Please enter their address... \n"),
        "Notes": input("Please enter any notes... \n")
    }

    with open(f"{address_book}.json", 'a+') as book:
        json.dump(entry, book)

    print("New entry added!")


def prompt_user_options(central_directory: list):
    """

    :param central_directory:
    :return:
    """
    pass
    # add_contact()


def get_contact_books(file):
    """

    :param file:
    :return:
    """
    contact_types = []

    try:
        with open(f"{file}.txt", 'r') as central:
            contact_types = central.readlines()

    except FileNotFoundError:
        print("No contact records found.\n")

    return contact_types



def contact_book(*file_name):
    """
    Read central directory and create one if necessary.

    :param file_name: a tuple
    :pre-condition: file_name may be empty or contain file names in string format
    :pre-condition: first item of file_name, if any, must be the name of the central directory of contact sub-lists
    :post-condition: the contents of file_name, if any, drive the rest of the program
    :return: None
    """
    # Allow user to choose central directory file - use default if none provided
    # contact_types = []

    if len(file_name) == 0:
        central_file = "central"

    else:
        central_file = file_name[0]

    # Try to open central - display existing file contents, if any (in else block)
    # try:
    #     with open(f"{central_file}.txt", 'r') as central:
    #         contact_types = central.readlines()
    #
    # except FileNotFoundError:
    #     print("No contact records found.\n")
    contact_types = get_contact_books(central_file)

    # If no file contents - get user to create new
    if len(contact_types) > 0:
        # Create new central file/directory

        prompt_user_options(contact_types)

    else:
        create_new_file(central_file, True, central_file)
        prompt_new_book(contact_types)


def main():
    """
    Drive the program.

    """
    if len(sys.argv) == 1:
        contact_book()

    else:
        contact_book(sys.argv[1:])


if __name__ == "__main__":
    main()
