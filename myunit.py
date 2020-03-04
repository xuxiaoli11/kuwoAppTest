import unittest
from desired_caps import appium_desired
import logging
from time import sleep
import warnings


class StartEnd(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        logging.info('========setUp========')
        self.driver = appium_desired()
        sleep(5)

    def tearDown(self):
        logging.info('========tearDown========')
        sleep(5)
        self.driver.close_app()
