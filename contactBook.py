# import necessary modules
import sys
import json
import io


# -----------------------------------------------------------------------------------------------
# These functions are for the general operation of the program
# -----------------------------------------------------------------------------------------------
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


def input_selector(categories: list):

    choice = input()

    if choice not in [str(number) for number in range(1, len(categories) + 1)]:
        print("Invalid input. Please enter numeric values only.\n")

    else:
        choice = int(choice)
        print(f"Wonderful. You have selected {categories[choice - 1]}.")
        return categories[choice - 1].strip()


def contact_book_choice(current_file: list):
    """
    Get user's choice of categories for new contact book.

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
    choice = ''
    while not choice:
        print("Please choose a new sub-category: \n")
        display_contact_types(categories)
        choice = input_selector(categories)

    return choice


def get_contact_books(file):
    """
    Create list out of books in main contact book directory.

    :param file: a string
    :pre-condition: file must be a string representing the name of a text file containing all contact books for the user
    :post-condition: a list is created containing the names of the user's contact books
    :return: a list
    """
    contact_types = []

    try:
        with open(f"{file}.txt", 'r') as central:
            contact_types = central.readlines()

    except FileNotFoundError:
        print("No contact records found.\n")

    return contact_types


def prompt_user_options(central_directory: str):
    """
    Allow user to add, view, edit, and delete

    :param central_directory: a string
    :pre-condition: main_directory must be a string representing the name of the central directory file
    :post condition: potential changes to the user's various contact books
    :return: None
    """
    function_list = [add_contact, view_contacts, edit_contact]
    books = get_contact_books(central_directory)
    print("Which book do you want to use?\n")
    book_choice_one = ''
    book_choice_two = None

    # Determine what book the user wants to work with
    while not book_choice_one:
        display_contact_types(books)
        book_choice_one = input_selector(books)

    # Determine what the user wants to do
    while not book_choice_two:
        display_contact_types(function_list)
        book_choice_two = input_selector(function_list)

    # Call applicable contact book interface
    book_choice_two(book_choice_one)

# -----------------------------------------------------------------------------------------------
# These functions relate to the creation of new client books
# -----------------------------------------------------------------------------------------------
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
        if category_type == 'json':
            json.dump({}, new_file)
        else:
            new_file.write("")

    # If this is a sub-file, add it to our central directory
    if file_type is False:
        with open(f"{central}.txt", 'a+') as central:
            central.write(f"{new_file_name}\n")

        print("New sub-file created!\n")


def prompt_new_book(contact_sublist: list, main_directory: str):
    """
    Get user's choice for new sub-book of contacts.

    :param contact_sublist: a list
    :param main_directory: a string
    :pre-condition: contact_sublist must be a list of the current, active contact sub-books in the central directory
    :pre-condition:
    :post-condition: a new sub-book file is created, added to the central directory
    :return: None
    """
    # If no other books exist
    if len(contact_sublist) == 0:
        print("Hello! you don't seem to have any entries in your address book. Let's start with making a new category.")

    user_choice = contact_book_choice(contact_sublist)

    # Create new file with chosen category name
    create_new_file(user_choice)

    # Add file to central directory

    # Provide the user with their options for adding, revising, viewing their contacts
    prompt_user_options(main_directory)


# -----------------------------------------------------------------------------------------------
# These functions relate to adding contacts to books
# -----------------------------------------------------------------------------------------------
def add_contact(address_book: str):
    """
    Add a contact entry to a sub-book.

    :param address_book: a string
    :pre-condition: address_book must be the name of the sub-book that the entry is to be added to
    :post-condition: new contact json object is added to the address sub-book
    :return: None
    """
    entry = {
        input("Please enter your contact's last name... \n"):
            {
                "First name": input("Please enter their first name... \n"),
                "Number": input("Please enter their number... \n"),
                "Address": input("Please enter their address... \n"),
                "Notes": input("Please enter any notes... \n")
            }
    }

    with open(f"{address_book}.json", 'r+') as book:
        # Read json file to variable
        book_json = json.load(book)
        # Update dictionary with new entry
        book_json.update(entry)
        # Reset file pointer to 0
        book.seek(0)
        # Add updated dictionary to json file as object, prettify it along the way
        json.dump(book_json, book, sort_keys=True, indent=4)

    print("New entry added!")


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
        main_directory = "central"

    else:
        main_directory = file_name[0]

    # Try to open central - display existing file contents, if any (in else block)
    contact_types = get_contact_books(main_directory)

    # If no file contents - get user to create new
    if len(contact_types) > 0:
        # Create new central file/directory

        prompt_user_options(main_directory)

    else:
        create_new_file(main_directory, True, main_directory)
        prompt_new_book(contact_types, main_directory)


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
