import unittest
from nmaplite.scanner import Scanner

class TestScanner(unittest.TestCase):

    def setUp(self):
        self.scanner = Scanner()

    def test_tcp_scan(self):
        result = self.scanner.tcp_scan('127.0.0.1', [80, 443])
        self.assertIsInstance(result, dict)
        self.assertIn(80, result)
        self.assertIn(443, result)

    def test_syn_scan(self):
        result = self.scanner.syn_scan('127.0.0.1', [22, 80])
        self.assertIsInstance(result, dict)
        self.assertIn(22, result)
        self.assertIn(80, result)

    def test_service_detection(self):
        result = self.scanner.service_detection('127.0.0.1', [80])
        self.assertIsInstance(result, dict)
        self.assertIn(80, result)

if __name__ == '__main__':
    unittest.main()