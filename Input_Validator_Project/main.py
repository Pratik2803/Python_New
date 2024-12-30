from validators.string_validator import StringValidtor
from validators.number_validator import NumberValidator
from validators.email_validator import EmailValidtor
from utils.exception_utils.custom_exceptions import ValidationError

if __name__ == '__main__':

    try:
        string_validator = StringValidtor()
        print(string_validator.validate("Hello"))
        # print(string_validator.validate(1234124))

        number_validator = NumberValidator(min_number=1, max_number=100)
        # print(number_validator.validate(101))
        # print(number_validator.validate("Hello"))
        print(number_validator.validate(99))

        email_validator = EmailValidtor()
        print(email_validator.validate("test@gmail.com"))
        print(email_validator.validate("Fuck You."))

    except ValidationError as e:
        print(f"Validation failed {e}")
