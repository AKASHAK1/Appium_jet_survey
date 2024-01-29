from appium import webdriver
from configuration_files import DeviceConfig as dc


class Driver:
    desired_caps = {}
    driver = None

    def get_driver_method(self):
        self.desired_caps['platformName'] = dc.platformVersion
        self.desired_caps['platformVersion'] = dc.platformVersion
        self.desired_caps['deviceName'] = dc.deviceName
        self.desired_caps['automationName'] = dc.automationName
        self.desired_caps['app'] = dc.app
        self.desired_caps['appPackage'] = dc.appPackage
        self.desired_caps['appActivity'] = dc.appActivity
        self.desired_caps['autoGrantPermissions'] = dc.autoGrantPermissions
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desired_caps)
        return self.driver
