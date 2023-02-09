import pytest
from modules.ui.page_objects.sign_in_page import SignInPage


@pytest.mark.ui
def test_github_wrong_login():

    sign_in = SignInPage()

    sign_in.login_attempt("wrongname", "wrongpass")

    assert sign_in.check_title()

    sign_in.close()
