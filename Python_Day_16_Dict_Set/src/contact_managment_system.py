from typing import Dict, List
from src.contact import Contact
from src.validator import Validator
import pandas as pd


class ContactManagmentSystem:
    """
    Responsible for Managing contacts 

    Adding a new contact
    """

    def __init__(self) -> None:
        self.contacts: Dict[str, Contact] = {}

    def add_contact(self, name: str, email: str, phone: str, category: str) -> None:

        if name in self.contacts:
            raise ValueError("Contact already exists.")
        self.contacts[name] = Contact(name, email, phone, category)

    def remove_contact(self, name: str) -> None:
        if name not in self.contacts:
            raise KeyError("Contact doesn't exists")
        del self.contacts[name]

    def update_contact(self, name: str, **kwargs) -> None:

        if name not in self.contacts:
            raise KeyError("Contact doesn't exists")

        for field, value in kwargs.items():
            if value is not None:
                if field.lower() == 'email':
                    self.contacts[name].email = Validator.validate_email(value)
                elif field.lower() == 'phone':
                    self.contacts[name].phone = Validator.validate_phone_no(
                        value)
                elif field.lower() == 'category':
                    self.contacts[name].category = Validator.validate_category(
                        value)
                else:
                    raise ValueError(f"Invalid field {
                                     field} for contact update")

    def seacrh_contact(self, query: str) -> List[Contact]:
        """
        Search based on generic string
        """
        if not query:
            raise ValueError("Search query can't be empty")

        results = []
        query = query.lower()
        for contact in self.contacts.values():
            if (
                contact.name.lower() == query or
                contact.email.lower() == query or
                contact.phone.lower() == query or
                contact.category.lower() == query
            ):
                results.append(contact)

        return results

    def group_by_category(self) -> Dict[str, Dict[str, Contact]]:
        grouped_contacts = {}

        for name, contact in self.contacts.items():
            category = contact.category

            if category not in grouped_contacts:
                grouped_contacts[category] = {}
            grouped_contacts[category][name] = contact

        return grouped_contacts

    def export_to_csv(self, file_name: str) -> None:

        data = [{
            "name": contact.name,
            "email": contact.email,
            "phone": contact.phone,
            "category": contact.category
        }
            for contact in self.contacts.values()
        ]

        df = pd.DataFrame(data)
        df.to_csv(path_or_buf=file_name, index=False)

    def import_from_csv(self, file_name: str) -> None:
        df = pd.read_csv(file_name)
        for _, row in df.iterrows():
            self.contacts[row['name']] = Contact(row['name'], row['email'],
                                                 row['phone'], row['category'])
