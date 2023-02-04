import pytest
from modules.common.database import Database

@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


def test_check_all_users():
    pass


def test_check_user_sergii():
    pass


def test_product_qnt_update():
    pass


def test_product_insert():
    pass


def test_product_delete():
    pass


def test_detailed_orders():
    pass
