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


def new_sublist(current_file: list):
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

        if choice not in [number for number in range(1, len(categories) + 1)]:
            print("Invalid input. Please enter numeric values only.\n")

        else:
            choice = int(choice)
            print(f"Wonderful. You have selected {categories[choice - 1]}.")
            return categories[choice - 1]


def prompt_new_book(contact_sublist: list):
    """

    :return:
    """
    # If no other books exist
    if len(contact_sublist) == 0:
        print("Hello! you don't seem to have any entries in your address book. Let's start with making a new category.")

    user_choice = new_sublist(contact_sublist)


def prompt_user_options(main_directory: list):
    pass


def contact_book(*file_name):
    """

    :param file_name: a tuple
    :pre-condition: file_name may be empty or contain file names in string format
    :pre-condition: first item of file_name, if any, must be the name of the central directory of contact sub-lists
    :post-condition: the contents of file_name, if any, drive the rest of the program
    :return: None
    """
    # Allow user to choose main directory file - use default if none provided
    contact_types = []

    if len(file_name) == 0:
        main_file = "central"

    else:
        main_file = file_name[0]

    # Try to open central - display existing file contents, if any (in else block)
    try:
        with open(f"{main_file}.txt", 'r') as central:
            contact_types = central.readlines()

    except FileNotFoundError:
        print("No contact records found.\n")

    # If no file contents - get user to create new
    if len(contact_types) > 0:
        prompt_user_options(contact_types)

    else:
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
