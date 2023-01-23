# class User:
#     def __init__(self) -> None:
#         self.name = 'Roman'
#         self.second_name = 'Chornyi'

# user = User()

# def test_remove_name():
#     user.name = ''
#     assert user.name == ''

# def test_name():
#     assert user.name == 'Roman'

# def test_second_name():
#     assert user.second_name == 'Chornyi'


import pytest


class User:
    def __init__(self) -> None:
        self.name = 'Roman'
        self.second_name = 'Chornyi'


@pytest.fixture
def user():
    return User()


def test_remove_name(user):
    user.name = ''
    assert user.name == ''


def test_name(user):
    assert user.name == 'Roman'


def test_second_name(user):
    assert user.second_name == 'Chornyi'


def test_change_name():
    user = User()
    user.create()

    assert user.name == 'Roman'
    user.remove()


def test_change_second_name():
    user = User()
    user.create()

    assert user.second_name == 'Chornyi'
    user.remove()
