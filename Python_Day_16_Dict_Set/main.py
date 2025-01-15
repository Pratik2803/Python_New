from src.contact_managment_system import ContactManagmentSystem


def main():
    # Create an instance of the ContactManagementSystem
    cms = ContactManagmentSystem()

    # Adding some contacts
    cms.add_contact("Alice", "alice@example.com", "1234567890", "Friend")
    cms.add_contact("Bob", "bob@example.com", "0987654321", "Work")
    cms.add_contact("Charlie", "charlie@example.com", "1231231234", "Friend")
    cms.add_contact("David", "david@example.com", "4564564567", "Work")
    cms.add_contact("Eve", "eve@example.com", "7897897890", "Family")

    # Updating a contact
    cms.update_contact(
        "Alice", email="bob@example.com")

    # Deleting a contact
    cms.remove_contact("Bob")

    # Searching for a contact
    results = cms.seacrh_contact("alice")
    print("Search Results:")
    for contact in results:
        print(f"Name: {contact.name}, Email: {contact.email}, Phone: {
              contact.phone}, Category: {contact.category}")

    # Grouping contacts by category
    grouped_contacts = cms.group_by_category()
    print("\nGrouped Contacts:")
    for category, contacts in grouped_contacts.items():
        print(f"Category: {category}")
        for name, contact in contacts.items():
            print(f" - {name}: {contact.email}, {contact.phone}")

    # Exporting contacts to CSV
    cms.export_to_csv("contacts.csv")
    print("\nContacts exported to 'contacts.csv'.")

    # Importing contacts from CSV
    cms.import_from_csv("contacts.csv")
    print("\nContacts imported from 'contacts.csv'.")


if __name__ == '__main__':
    main()
