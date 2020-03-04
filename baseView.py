import logging


class BaseView(object):
    def __init__(self, driver):
        self.driver = driver  # 定义属性

    def find_element(self, *loc):
        return self.driver.find_element(*loc)  # 定义方法

    def get_size(self):
        logging.info("==========get size==========")
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y  # 获取屏幕尺寸


