# Contents of /nmaplite/nmaplite/tests/test_cli.py

import unittest
from nmaplite.cli import main

class TestCLI(unittest.TestCase):

    def test_help_command(self):
        """Test the help command output."""
        result = main(['--help'])
        self.assertIn('usage:', result)

    def test_scan_command(self):
        """Test the scan command with a valid target."""
        result = main(['scan', '127.0.0.1'])
        self.assertEqual(result.exit_code, 0)

    def test_invalid_command(self):
        """Test the command with an invalid option."""
        result = main(['invalid_command'])
        self.assertNotEqual(result.exit_code, 0)

if __name__ == '__main__':
    unittest.main()