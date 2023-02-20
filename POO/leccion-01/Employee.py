from Person import Person


class Employee(Person):
    def __init__(self, name: str = None, last_name: str = None, dni: str = None, email: str = None, salary: float = 0.0):
        super().__init__(name, last_name, dni, email)
        self.salary = salary
