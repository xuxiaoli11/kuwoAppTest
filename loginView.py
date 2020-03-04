import logging
from common_fun import Common
from desired_caps import appium_desired
from selenium.webdriver.common.by import By
from time import sleep


class LoginView(Common):
    clickloginBtn = (By.NAME, '点击登录')
    kuwologinBtn = (By.NAME, '酷我登录')
    username_type = (By.ID, 'cn.kuwo.player:id/login_et_username')
    password_type = (By.ID, 'cn.kuwo.player:id/login_et_password')
    loginBtn = (By.ID, 'cn.kuwo.player:id/text_login_btn')

    def login_action(self, username, password):
        self.driver.find_element(*self.clickloginBtn).click()
        self.driver.find_element(*self.kuwologinBtn).click()
        logging.info('==========login==========')
        logging.info('input username:%s', username)
        self.driver.find_element(*self.username_type).send_keys(username)

        logging.info('input password:%s', password)
        self.driver.find_element(*self.password_type).send_keys(password)

        logging.info('click loginBtn')
        self.driver.find_element(*self.loginBtn).click()
        logging.info('login finished')


if __name__ == '__main__':
    driver = appium_desired()
    com = Common(driver)
    sleep(5)
    com.swipeLr(0.1, 0.9, 0.5)
    lo = LoginView(driver)
    lo.login_action('80403765', 'zaijian11')



