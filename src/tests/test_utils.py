import unittest
from utils.pages import has_valid_extension


class HasValidExtensionTestCase(unittest.TestCase):

    def test_has_valid_extension_with_md_file(self):
        file_name = 'example.md'
        result = has_valid_extension(file_name)
        self.assertTrue(result)

    def test_has_valid_extension_with_html_file(self):
        file_name = 'index.html'
        result = has_valid_extension(file_name)
        self.assertTrue(result)

    def test_has_valid_extension_with_other_extension(self):
        file_name = 'script.js'
        result = has_valid_extension(file_name)
        self.assertFalse(result)

    def test_has_valid_extension_with_mixed_case_extension(self):
        file_name = 'example.MD'
        result = has_valid_extension(file_name)
        self.assertTrue(result)

    def test_has_valid_extension_with_no_extension(self):
        file_name = 'README'
        result = has_valid_extension(file_name)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
