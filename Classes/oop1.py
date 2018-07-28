''' from http://python-textbok.readthedocs.io/en/1.0/Classes.html
'''
# 1. defining and using a Class
import datetime # we will use this for date objects

class Person:    #object

    def __init__(self, name, surname, birthdate, address, telephone, email): # __method__ (object itself, other parameters)
        self.name = name     # attribute = parameter (info is storred in object's attributes)
        self.surname = surname
        self.birthdate = birthdate # birthdate is itself an object (the date class is defined in the datetime module)

        self.address = address
        self.telephone = telephone
        self.email = email

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age

person = Person(
    "Jane",
    "Doe",
    datetime.date(1992, 3, 12), # year, month, day
    "No. 12 Short Street, Greenville",
    "555 456 0987",
    "jane.doe@example.com"
)     # person = instance of the Person class

print(person.name)
print(person.email)
print(person.age())
