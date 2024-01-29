import time
from base.Base import Base
import utils.CustomLogger as cl


class LoginApp(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    email = ('xpath', '//android.widget.EditText')
    email_continue = ('xpath', '//android.widget.Button[@text="CONTINUE"]')
    sign_in_email = ('xpath', '//android.view.ViewGroup[@resource-id="com.example.compose.jetsurvey:id/sign_in_fragment'
                              '"]/android.view.View/android.widget.EditText[1]')
    password = ('xpath', '//android.view.ViewGroup[@resource-id="com.example.compose.jetsurvey:id/sign_in_fragment'
                         '"]/android.view.View/android.widget.EditText[2]')

    signin_button = ('xpath', '//android.widget.Button[@text="Sign in"]')

    def input_email(self):
        time.sleep(2)
        self.send_keys(self.email, "akash@gmail.com")
        cl.allure_logs("Entered username")

    def click_continue_button(self):
        self.click(self.email_continue)
        cl.allure_logs("Clicked on continue button")

    def input_sign_in_email(self):
        time.sleep(2)
        self.send_keys(self.sign_in_email, "akash@gmail.com")
        cl.allure_logs("Entered email")

    def input_password(self):
        time.sleep(2)
        self.send_keys(self.password, "akash@123")
        cl.allure_logs("Entered password")

    def click_signin_button(self):
        self.click(self.signin_button)
        cl.allure_logs("Clicked on signin button")

    def login_sup(self):
        self.input_email()
        self.click_continue_button()
        self.input_sign_in_email()
        self.input_password()
        self.click_signin_button()
        cl.allure_logs("User signed in successfully")
