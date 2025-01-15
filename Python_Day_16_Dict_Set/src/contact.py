from src.validator import Validator


class Contact:
    """
    Responsible for a single contact
    """

    def __init__(self, name: str, email: str, phone: str, category: str) -> None:
        """
        Initialize a contact with validated fields.

        Args:
            name(str) : name of the contact
            email(str): email of the contact
            phone(str) : phone no of the contact
            category(str) : Category of the contact
        """
        self.name = Validator.validate_name(name)
        self.email = Validator.validate_email(email)
        self.phone = Validator.validate_phone_no(phone)
        self.category = Validator.validate_category(category)
