from Person import Person


class Client(Person):
    def __init__(self, name: str = None, last_name: str = None, dni: str = None, email: str = None, type: str = None):
        super().__init__(name, last_name, dni, email)
        self.type = type