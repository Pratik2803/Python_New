import re


class Validator:
    """ 
    Responsible for validating contact attributes. 
    """

    @staticmethod
    def validate_name(name: str) -> str:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        return name

    @staticmethod
    def validate_category(category: str) -> str:
        if not isinstance(category, str) or not category.strip():
            raise ValueError("Category must be a non-empty string")
        return category

    @staticmethod
    def validate_email(email: str) -> str:
        if not isinstance(email, str) or not email.strip():
            raise ValueError("Email must be a non-empty string")

        email_regex = r'^[A-Za-z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

        if not re.fullmatch(pattern=email_regex, string=email):
            raise ValueError("Not a valid email address")

        return email

    @staticmethod
    def validate_phone_no(phone: str) -> str:
        if not isinstance(phone, (str, int)):
            raise ValueError("Phone no. must be of string or integer type")

        if isinstance(phone, str):
            if not phone.strip():
                raise ValueError("Phone no. must be a non-empty string")

        phone_regex = r'^\+?(\d{1,3})?[-. (]*\d{3}[-. )]*\d{3}[-. ]*\d{4}$'

        phone_str = str(phone)
        if not re.match(pattern=phone_regex, string=phone_str):
            raise ValueError("Not a valid phone number")

        return phone
