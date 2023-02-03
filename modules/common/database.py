import sqlite3


class Database:

    def __init__(self) -> None:
        self.connection = sqlite3.connect(r'/home/romcha/projects/qa_auto_23_rch' + r'/become_qa_auto.bd')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Querry = 'SELECT sqlite_version();'
        self.cursor.execute(sqlite_select_Querry)
        record = self.cursor.fetchall()
        print(f'Connected successfully. SQLite Database version is {record}')

    def get_all_users(self):
        pass

    def get_user_address_by_name(self):
        pass

    def update_product_qnt_by_id(self):
        pass

    def select_product_qnt_by_id(self):
        pass

    def insert_product(seld):
        pass

    def delete_product(self):
        pass

    def get_detailed_orders(self):
        pass
