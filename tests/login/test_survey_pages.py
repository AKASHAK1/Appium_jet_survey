from appium import webdriver
import time
import unittest
from pages.auth.login import LoginApp
from pages.survey.survey_pages import SurveyModule


class Login(unittest.TestCase, LoginApp, SurveyModule):

    def setUp(self):
        desired_cap = {
            "deviceName": "3549df35",
            "platformName": "Android",
            "app": "C:/test/jetsurvey-debug.apk",
            'autoGrantPermissions': "true"
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

    def test_survey_module(self):
        self.driver.implicitly_wait(5)
        time.sleep(1)
        self.login_sup()
        time.sleep(1)
        self.survey_module()

    def teardown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
