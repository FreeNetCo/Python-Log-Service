#!/usr/bin/python
__author__ = 'anonymous'
__version__ = '1.0.0'

import pydoc
import logging


class DroLogger(object):

    def __init__(self):
        logging.basicConfig(
            format='%(asctime)s %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p',
            filename='app.log',
            level=logging.DEBUG
        )

    @classmethod
    def log(cls, severity, msg):
        """
        DroLogger.log()
        Handles logging different severity types
        :param cls: this class
        :param severity: the log level severity for this event
        :param msg: the message to be logged
        :return boolean: return true if we were able to successfully log the message
        """
        severity = str.lower(severity)

        if severity == 'debug':
            DroLogger._debug(msg)
        elif severity == 'info':
            DroLogger._info(msg)
        elif severity == 'warn':
            DroLogger._warn(msg)
        elif severity == 'error':
            DroLogger._error(msg)
        elif severity == 'critical':
            DroLogger._critical(msg)
        else:
            raise Exception(
                'A call to DroLogger.log() was raised without providing a valid severity type!\n'
                'Severity type provided: {}'.format(severity)
            )
        return True

    @classmethod
    def _debug(cls, msg):
        """
        Called by DroLogger.log() internally
        Logs the debug message using the logging.basicConfig()
        and prints the message to the console
        :param cls: The abstract method's parent
        :param msg: A user-specified debug message
        :return:
        """
        logging.debug(msg)
        print(msg)

    @classmethod
    def _info(cls, msg):
        """
        Called by DroLogger.log() internally
        Logs the info message using the logging.basicConfig()
        and prints the message to the console
        :param cls: This abstract method's parent class
        :param msg: A user-specified info message
        """
        logging.info(msg)
        print(msg)

    @classmethod
    def _warn(cls, msg):
        """
        Called by DroLogger.log() internally
        Logs the warning message using the logging.basicConfig()
        and prints the message to the console
        :param cls: This abstract method's parent class
        :param msg: A user-specified info message
        """
        logging.warn(msg)
        print(msg)

    @classmethod
    def _error(cls, msg):
        """
        Called by DroLogger.log() internally
        Logs the error message using the logging.basicConfig()
        and prints the message to the console
        :param cls: This abstract method's parent class
        :param msg: A user-specified info message
        """
        logging.error(msg)
        print(msg)

    @classmethod
    def _critical(cls, msg):
        """
        Called by DroLogger.log() internally
        Logs a critical error message using the logging.basicConfig()
        and prints the message to the console
        :param cls: This abstract method's parent class
        :param msg: A user-specified info message
        """
        logging.critical(msg)
        print(msg)


def main():
    DroLogger.log('debug', 'A debug message has been caught.')
    DroLogger.log('info', 'An info message has been caught.')
    DroLogger.log('warn', 'A warning has been caught.')
    DroLogger.log('error', 'An error has been caught.')
    DroLogger.log('critical', 'A critical error has been caught.')


if __name__ == "__main__": main()