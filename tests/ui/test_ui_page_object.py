import pytest
from selenium import webdriver
from modules.ui.page_objects.sign_in_page import SignInPage
from modules.ui.page_objects.sign_up_page import SignUpPage
import random

browser = webdriver.Chrome()


@pytest.mark.signin
def test_github_wrong_login():

    sign_in = SignInPage()

    # Failed login attempt
    sign_in.login_attempt("wrongname", "wrongpass")
    assert sign_in.check_title("Sign in to GitHub · GitHub")

    sign_in.close()


@pytest.mark.signup
def test_git_hub_signup():

    randomNumber = random.randint(100, 200)
    email = "romchablack" + str(randomNumber) + "@gmail.com"
    password = "12345678"

    sign_up = SignUpPage()

    sign_up.signup_attempt(email, password)
