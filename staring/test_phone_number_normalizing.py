import unittest


def normalize_phone_number(phone_number: str):
    number_without_spaces = phone_number.replace("-", "")
    if " " in number_without_spaces:
        return number_without_spaces.replace(" ", "")
    if len(number_without_spaces) > 9:
        return "number is too long"
    if len(number_without_spaces) < 9:
        return "number is too short"

    return number_without_spaces

class TestPhoneNumberNormalization(unittest.TestCase):

    def test_normalized_number_have_no_hyphens(self) -> None:
        self.assertEqual('123456789', normalize_phone_number('123-456-789-'))

    def test_normalized_number_has_no_spaces(self) -> None:
        self.assertEqual('123456789', normalize_phone_number('123 456  789'))

    def test_normalized_number_has_no_spaces_nor_hyphens(self) -> None:
        self.assertEqual('123456789', normalize_phone_number('123 456-789'))

    def test_number_to_be_normalized_should_have_exactly_nine_digits(self) -> None:
        self.assertEqual('number is too long', normalize_phone_number('12345678910'))
        self.assertEqual('number is too long', normalize_phone_number('12345 78910'))
        self.assertEqual('number is too short', normalize_phone_number('12345678'))

    def test_number_can_only_contain_digits(self) -> None:
        self.assertEqual("number contains invalid characters 'abc'", normalize_phone_number('1a34b67c9'))
        self.assertEqual("number contains invalid characters 'xyz'", normalize_phone_number('1x34y67z9'))
