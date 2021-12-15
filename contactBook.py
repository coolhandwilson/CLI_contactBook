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


def new_sublist(new_file: bool = False):
    categories = ['Friends', 'Business', 'School', 'Family']

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


def prompt_new_book(*file_name: tuple):
    """

    :return:
    """
    print("Hello! you don't seem to have any entries in your address book. Let's start with making a new category.")
    if len(file_name) == 0:
        user_choice = new_sublist()


def prompt_user_options(main_directory):
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
    if len(file_name) == 0:
        file_name = "central"

    # Try to open central - display existing file contents, if any (in else block)
    try:
        with open(f"{file_name[0]}.txt", 'r') as central:
            contact_types = central.readlines()

    except FileNotFoundError:
        print("No contact records found.\n")

    else:
        display_contact_types(contact_types)

    # If no file contents - get user to create new
    if len(contact_types) == 0:
        prompt_new_book()

    else:
        prompt_user_options(file_name)


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
