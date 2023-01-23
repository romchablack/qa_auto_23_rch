class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = 'Roman'
        self.second_name = 'Chornyi'

    def remove(self):
        self.name = ''
        self.second_name = ''
