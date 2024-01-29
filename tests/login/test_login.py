from appium import webdriver
import time
import unittest
from pages.auth.login import LoginApp


# from pages.SFC.sfc_lines import my_lin        es

class Login(unittest.TestCase, LoginApp):

    def setUp(self):
        desired_cap = {
            "deviceName": "3549df35",
            "platformName": "Android",
            "app": "C:/test/jetsurvey-debug.apk",
            'autoGrantPermissions': "true"
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

    def test_my_lines_machine(self):
        self.driver.implicitly_wait(5)
        time.sleep(2)
        self.login_sup()

    def teardown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
