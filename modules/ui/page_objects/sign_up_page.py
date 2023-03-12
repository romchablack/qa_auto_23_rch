from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from modules.ui.page_objects.base_page import BasePage


import time


class SignUpPage(BasePage):
    url = "https://github.com/signup"

    def __init__(self) -> None:
        super().__init__()
        self.driver.get(self.url)

    def signup_attempt(self, email, password):

        # email field
        locator = (By.ID, "email")
        email_fld = WebDriverWait(
            self.driver, 10).until(
            EC.visibility_of_element_located(locator))
        email_fld.clear()
        email_fld.send_keys(email)
        time.sleep(3)

        # email check
        try:
            email_check = self.driver.find_element(By.CSS_SELECTOR, "p.mb-0")
            if email_check.is_displayed():
                print(email_check.text)
        except NoSuchElementException:
            # Continue button
            continue_button = self.driver.find_element(By.XPATH, "//div[@id='email-container']/div/button")
            continue_button.click()
            time.sleep(3)

        password_fld = self.driver.find_element(By.ID, "password")
        password_fld.clear()
        password_fld.send_keys(password)
        time.sleep(3)