import unittest
from unittest.mock import patch
from utils.argparser import parse_args


class TestParseArgs(unittest.TestCase):
    def test_parse_args_with_args(self):
        args = ['--path', 'static', '--port', '8000']
        res = parse_args(args)
        self.assertEqual(res.path, 'static')
        self.assertEqual(res.port, 8000)


if __name__ == '__main__':
    unittest.main()
