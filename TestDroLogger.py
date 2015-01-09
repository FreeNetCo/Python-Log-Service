#!/usr/bin/python
__author__ = 'anonymous'

import unittest
from DroLogger import DroLogger


class TestLoggerFunctions(unittest.TestCase):

    def setUp(self):
        # List of severity types to loop over in our tests
        self.severity = ['debug', 'info', 'warn', 'error', 'critical']
        # Default message to be 'logged'
        self.msg = 'A message worth logging'

    def test_logging_successful(self):
        print('test_logging_successful:')
        logger = DroLogger()
        for sev in self.severity:
            self.assertTrue(logger.log(sev, self.msg))
        print('Test successful.\n')

    def test_logging_errors(self):
        print('test_logging_errors:')
        logger = DroLogger()
        # Attempt to log an invalid severity type
        self.severity.extend("0")
        self.assertRaises(Exception, logger.log, self.severity[-1], self.msg)
        print('An exception was caught, hooray!\n')

if __name__ == "__main__": unittest.main()