import logging
from common_fun import Common
from desired_caps import appium_desired


class SwipeView(Common):

    def swipeLeft(self, xs, xe, y):
        l = Common.get_size
        x1 = int(l[0] * xs)
        y1 = int(l[1] * y)
        x2 = int(l[0] * xe)
        self.driver.swipe(x1, y1, x2, y1, 1000)  # 左滑

    def swipeRight(self, ys, ye, x):
        l = Common.get_size
        x1 = int(l[0] * x)
        y1 = int(l[1] * ys)
        x2 = int(l[0] * ye)
        self.driver.swipe(x2, y1, x1, y1, 1000)  # 右滑
