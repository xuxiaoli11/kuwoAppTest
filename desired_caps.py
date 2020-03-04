import yaml
import logging.config
from appium import webdriver
from time import sleep

CON_LOG = 'E:\studyxxl\Appium+Python\kuwoAppTest\log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


def appium_desired():
    stream = open('E:\studyxxl\Appium+Python\kuwoAppTest\desired_caps.yaml', 'r')
    data = yaml.load(stream, Loader=yaml.FullLoader)

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['noRest'] = data['noRest']

    logging.info('start app...')
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)

    # driver.implicitly_wait(10)
    sleep(5)
    return driver


if __name__ == '__main__':
    appium_desired()
