from selenium.webdriver.common.by import By
from modules.ui.page_objects.base_page import BasePage
import time


class SignInPage(BasePage):
    def __init__(self) -> None:
        super().__init__()
        self.driver.get("https://github.com/login")

    def login_attempt(self, username, password):
        # find username field
        name_fld = self.driver.find_element(By.ID, "login_field")
        name_fld.clear()
        name_fld.send_keys(username)
        time.sleep(1)
        # find password field
        pass_fld = self.driver.find_element(By.ID, "password")
        name_fld.clear()
        pass_fld.send_keys(password)
        time.sleep(1)
        # find login button
        login_btn = self.driver.find_element(By.NAME, "commit")
        login_btn.click()
        time.sleep(1)

    def check_title(self):
        return "Sign in to GitHub" in self.driver.title
