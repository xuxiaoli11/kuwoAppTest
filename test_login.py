from myunit import StartEnd, dr
from loginView import LoginView
from common_fun import Common
from desired_caps import appium_desired
from time import sleep
import unittest
import logging


class TestLogin(StartEnd):
    driver = appium_desired()
    def test_login_1(self):
        logging.info('========test_login_1========')
        # driver = appium_desired()
        # sleep(5)
        # com = Common(driver)
        # com.swipeLr(0.1, 0.9, 0.5)
        Common.swipeLr(, 0.1, 0.5, 0.9)
        LoginView.login_action('80403765', 'zaijian11')
        # lo = LoginView(driver)
        # lo.login_action('80403765', 'zaijian11')


if __name__ == '__main__':
    unittest.main()
