import json

# Function to load contacts from a JSON file
def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts

# Function to save contacts to a JSON file
def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=2)

# Function to add a new contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")

    new_contact = {
        "name": name,
        "phone": phone,
    }

    contacts.append(new_contact)
    save_contacts(contacts)
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts():
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact['name']} - {contact['phone']}")

# Function to search contacts by name or phone number
def search_contact(query):
    results = [contact for contact in contacts if query.lower() in contact['name'].lower() or query in contact['phone']]
    return results

# Function to update contact details
def update_contact():
    view_contacts()
    index = int(input("Enter the index of the contact to update: ")) - 1

    if 0 <= index < len(contacts):
        field = input("Enter the field to update (name, phone, email, address): ")
        new_value = input(f"Enter new {field}: ")

        contacts[index][field] = new_value
        save_contacts(contacts)
        print("Contact updated successfully!")
    else:
        print("Invalid index.")

# Function to delete a contact
def delete_contact():
    view_contacts()
    index = int(input("Enter the index of the contact to delete: ")) - 1

    if 0 <= index < len(contacts):
        del contacts[index]
        save_contacts(contacts)  
        print("Contact deleted successfully!")
    else:
        print("Invalid index.")

# Main program
contacts = load_contacts()

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        query = input("Enter name or phone number to search: ")
        results = search_contact(query)
        if results:
            print("Search Results:")
            for result in results:
                print(f"{result['name']} - {result['phone']}")
        else:
            print("No matching contacts found.")
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
