from myunit import StartEnd
from loginView import LoginView
from common_fun import Common
from baseView import BaseView
from desired_caps import appium_desired
from time import sleep
import unittest
import logging


class TestLogin(StartEnd):
    def test_login_1(self):
        logging.info('========test_login_1========')
        driver = appium_desired()
        sleep(5)
        com = Common(driver)
        com.swipeLr(0.1, 0.9, 0.5)
        lo = LoginView(driver)
        lo.login_action('80403765', 'zaijian11')


if __name__ == '__main__':
    unittest.main()
