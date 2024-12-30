import unittest
from validators.string_validator import StringValidtor
from utils.exception_utils.custom_exceptions import ValidationError


class TestStringValidator(unittest.TestCase):
    """Unit tests for StringValidator."""

    def test_valid_string(self):
        validator = StringValidtor(min_length=1, max_length=6)
        self.assertTrue(validator.validate("Hello"))

    def test_not_string(self):
        validator = StringValidtor()

        with self.assertRaises(ValidationError):
            validator.validate(123)

    def test_less_than_min_length(self):
        validator = StringValidtor(min_length=5, max_length=10)

        with self.assertRaises(ValidationError):
            validator.validate("fuck")
