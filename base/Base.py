from utils.page_utils import PageUtils


class Base(PageUtils):
    def click(self, locator):
        self.click_element(locator)

    def send_keys(self, locator, text):
        self.send_value(locator, text)

    def wait_display(self, locator, timeout = 10):
        self.wait_visible(locator, timeout)