import time
import allure
from allure_commons.types import AttachmentType
from allure import attachment_type
from appium.webdriver.common.appiumby import AppiumBy
import utils.CustomLogger as cl
from selenium.common.exceptions import NoSuchElementException, WebDriverException


class PageUtils:
    log = cl.custom_logger()

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        method = locator[0]
        values = locator[1]
        if type(values) is str:
            return self.get_element_by_type(method, values)

        elif values is list:
            for _ in values:
                try:
                    return self.get_element_by_type(method, values)
                except NoSuchElementException:
                    pass
            raise NoSuchElementException

    # get element by locator type
    def get_element_by_type(self, method, value):
        if method == 'accessibility_id':
            return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, value)
        elif method == 'android':
            return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UISelector().%s' % value)
        elif method == 'iOS':
            return self.driver.find_element(AppiumBy.IOS_UIAUTOMATION, value)
        elif method == 'id':
            return self.driver.find_element(AppiumBy.ID, value)
        elif method == 'class_name':
            return self.driver.find_element(AppiumBy.CLASS_NAME, value)
        elif method == 'xpath':
            return self.driver.find_element(AppiumBy.XPATH, value)
        elif method == 'name':
            return self.driver.find_element(AppiumBy.NAME, value)
        elif method == 'text':
            return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("%s")' % value)
        else:
            raise Exception('Invalid locator method')

    # element _visible
    def is_visible(self, locator):
        locatorType = locator[0]
        locatorValue = locator[1]
        try:
            self.get_element(locator).is_displayed()
            self.log.info(
                " Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue +
                "is visible ")
            return True
        except NoSuchElementException:
            self.log.error(
                " Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue +
                " is not visible")
            self.takeScreenshot(locatorType)
            return False

    # wait if the locator is not visible
    def wait_visible(self, locator, timeout=10):
        i = 0
        while i != timeout:
            try:
                self.is_visible(locator)
                return self.get_element(locator)
            except NoSuchElementException:
                time.sleep(1)
                i += 1

            raise NoSuchElementException('Element never become visible: %s (%s)' % (locator[0], locator[1]))

    # clicks and taps
    def click_element(self, locator):
        locatorType = locator[0]
        locatorValue = locator[1]
        try:
            element = self.wait_visible(locator)
            element.click()
            self.log.info(
                "Clicked on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
        except(Exception,):
            self.log.error(
                "Unable to click on Element with LocatorType: " + locatorType + " and with the locatorValue :" +
                locatorValue)
            self.takeScreenshot(locatorType)
            assert False

    def tap_element(self, locator):
        element = self.wait_visible(locator)
        element.tap()

    # hide keyboard
    def hide_keyboard(self):
        try:
            time.sleep(1)
            self.driver.hide_keyboard()
        except WebDriverException:
            pass

    # send keys function to provide text to input box
    def send_value(self, locator, text):
        locatorType = locator[0]
        locatorValue = locator[1]
        try:
            element = self.wait_visible(locator)
            element.send_keys(text)
            self.log.info(
                "Send text  on Element with LocatorType: " + locatorType + " and with the locatorValue :" +
                locatorValue)
            self.hide_keyboard()
            time.sleep(1)
        except (Exception,):
            self.log.error(
                "Unable to send text on Element with LocatorType: " + locatorType + " and with the locatorValue :" +
                locatorValue)
            self.takeScreenshot(locatorType)

    # clear the values
    def clear(self, locator):
        element = self.wait_visible(locator)
        element.clear()
        time.sleep(0.5)

    # scrolling in Android
    def android_scroll(self, locator):
        for _ in range(15):
            x = 950
            try:
                value = self.get_element(locator).is_displayed()
                if value is True:
                    break
            except NoSuchElementException:
                self.driver.swipe(470, 1488, 470, x, 330)
                self.driver.implicitly_wait(2)
                continue

    def ios_scroll(self, locator):
        el = self.wait_visible(locator)
        self.driver.execute_script('mobile: scroll', {"element": el, "toVisible": True})

    def get_text(self, locator):
        element = self.wait_visible(locator)
        return element.text()

    def screenShot(self, screenshotName):
        fileName = screenshotName + "_" + (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshotDirectory = "../screenshots/"
        screenshotPath = screenshotDirectory + fileName
        try:
            self.driver.save_screenshot(screenshotPath)
            self.log.info("Screenshot save to Path : " + screenshotPath)

        except (Exception,):
            self.log.error("Unable to save Screenshot to the Path : " + screenshotPath)

    def takeScreenshot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)

    def keyCode(self, value):
        self.driver.press_keycode(value)
