contacts = []

def add_contact():
    name = input("Enter name: ")
    qq = input("Enter QQ number: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contact_info = {
        'name': name,
        'qq': qq,
        'phone': phone,
        'email': email
    }

    contacts.append(contact_info)
    print(f"\nAdded successfully: {contact_info['name']} !")
    return contact_info

def delete_contact():
    if not contacts:
        print("No contacts to delete.")
        return

    show_contacts()
    serial_number = int(input("Enter serial number you want to delete: "))
    if serial_number < 0 or serial_number >= len(contacts):
        print("Invalid serial number.")
    else:
        deleted_contact = contacts.pop(serial_number)
        print(f"Deleted successfully: {deleted_contact['name']}")

def modify_contact():
    if not contacts:
        print("No contacts to modify.")
        return

    show_contacts()
    serial_number = int(input("Enter serial number you want to modify: "))
    if serial_number < 0 or serial_number >= len(contacts):
        print("Invalid serial number.")
    else:
        print("The editable sub-items are as follows:")
        print("1. Name")
        print("2. QQ Number")
        print("3. Phone Number")
        print("4. Email")

        option = int(input("Enter the serial number you want to modify: "))
        if option >= 1 and option <= 4:
            keys = ["name", "qq", "phone", "email"]
            new_value = input(f"Please enter a new {keys[option - 1]}: ")
            if new_value.strip() != "":
                contacts[serial_number][keys[option - 1]] = new_value
                print("Modified successfully!")
            else:
                print("Modification canceled.")
        else:
            print("Error.")

def find_contact():
    if not contacts:
        print("No contacts to find.")
        return

    search_key = input("Please enter the search keyword (such as name, phone, etc.): ")
    found_contacts = []
    for contact in contacts:
        for value in contact.values():
            if search_key in str(value):
                found_contacts.append(contact)
                break
    if found_contacts:
        print("Found contact information:")
        for contact in found_contacts:
            print(contact)
    else:
        print("No contacts meeting the conditions were found.")

def show_contacts():
    if not contacts:
        print("There is currently no contact information.")
    else:
        print("All contact information:")
        for index, contact in enumerate(contacts):
            print(f"Serial number: {index}, Information: {contact}")

def main_menu():
    while True:
        print("\n======================================== Contact Management System ========================================\n")
        print("a: Add Contact")
        print("d: Delete Contact")
        print("c: Modify Contact")
        print("f: Find Contact")
        print("s: Show Contacts")
        choice = input("\nPlease enter your operation: ")
        if choice == "a":
            add_contact()
        elif choice == "d":
            delete_contact()
        elif choice == "c":
            modify_contact()
        elif choice == "f":
            find_contact()
        elif choice == "s":
            show_contacts()
        else:
            print("Input error. Please enter again.")

if __name__ == "__main__":
    main_menu()