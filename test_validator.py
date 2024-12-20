import unittest
from pydictvalidator.validator import validate_json

class TestValidator(unittest.TestCase):
    def test_valid_json(self):
        data = '{"key":"value"}'
        self.assertTrue(validate_json(data))
        
    def test_invalid_json(self):
        data = '{"key":"value"'
        self.assertFalse(validate_json(data))
        
if __name__ ="__main__":
    unittest.main()