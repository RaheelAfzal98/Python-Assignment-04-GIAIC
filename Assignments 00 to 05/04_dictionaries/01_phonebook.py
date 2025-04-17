# Problem Statement
# In this program we show an example of using dictionaries to keep track of information in a phonebook.


def collect_contacts():
    """
    Continuously ask the user for names and their corresponding phone numbers.
    Stop collecting when an empty name is entered.
    Return the filled contact book (dictionary).
    """
    contacts = {}  # Empty dictionary to store contacts

    while True:
        person = input("Enter a contact name (leave blank to finish): ")
        if person == "":
            break
        phone = input(f"Enter the phone number for {person}: ")
        contacts[person] = phone

    return contacts


def show_contacts(contacts):
    """
    Print all saved contacts and their numbers from the contact book.
    """
    print("\nContact List:")
    for person, number in contacts.items():
        print(f"{person}: {number}")


def search_contacts(contacts):
    """
    Let the user search for a contact's phone number by name.
    Stop when an empty name is entered.
    """
    print("\nSearch for contacts:")
    while True:
        search_name = input("Name to find (blank to stop): ")
        if search_name == "":
            break
        if search_name in contacts:
            print(f"Phone number for {search_name}: {contacts[search_name]}")
        else:
            print(f"{search_name} is not in your contacts.")


def main():
    contact_book = collect_contacts()
    show_contacts(contact_book)
    search_contacts(contact_book)


if __name__ == '__main__':
    main()
