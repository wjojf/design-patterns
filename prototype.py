from copy import deepcopy

class Address:
    def __init__(self, city, country):
        self.city = city 
        self.country = country
    
    def __str__(self):
        return f'{self.city}, {self.country}'

class Person:
    def __init__(self, name, address):
        self.name = name 
        self.address = address
    
    def __str__(self):
        return f'{self.name} lives at {self.address}'


john = Person('John', Address('London', 'UK'))

jane = deepcopy(john)
jane.name = 'Jane'
jane.address.city = 'Manchester'

print(john, '\n', jane)