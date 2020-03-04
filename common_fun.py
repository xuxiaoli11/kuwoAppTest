from baseView import BaseView
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
from desired_caps import appium_desired
from time import sleep


class Common(BaseView):
    # driver = appium_desired()

    def swipeLr(self, xs, xe, y):
        logging.info('========swipe lr========')
        l = BaseView.get_size(self)
        x1 = int(l[0] * xs)
        y1 = int(l[1] * y)
        x2 = int(l[0] * xe)
        self.driver.swipe(x1, y1, x2, y1, 1000)  # 左/右滑动

    def swipeUd(self, ys, ye, x):
        logging.info('========swipe ud========')
        l = BaseView.get_size(self)
        y1 = int(l[1] * ys)
        x1 = int(l[0] * x)
        y2 = int(l[1] * ye)
        self.driver.swipe(x1, y1, x1, y2, 1000)  # 上/下滑动


if __name__ == '__main__':
    driver = appium_desired()
    sleep(5)
    com = Common(driver)
    com.swipeLr(0.9, 0.1, 0.5)
    com.swipeUd(0.1, 0.9, 0.5)
