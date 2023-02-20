class Person:
    def __init__(self, name: str = None, last_name: str = None, dni: str = None, email: str = None):
        self.name = name
        self.last_name = last_name
        self.dni = dni
        self.email = email

    def __str__(self):
        return f'''Resume: 
        {self.name}
        {self.last_name}
        {self.email}
        '''
