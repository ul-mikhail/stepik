class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} лет"


person = Person("Vasya", 25)
print(person)  # Vasya, 25 лет

class MyClass:
    def __str__(self):
        return f'Метод __str__'

    def __repr__(self):
        return f'Метод __repr__'


test = MyClass()
print(test)           # Метод __str__
print(repr(test))     # Метод __repr__

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        return hash((self.name, self.age))

person1 = Person("Vasya", 25)
person2 = Person("Masha", 30)
person3 = Person("Masha", 30)

print(hash(person1))  # 8796873826
print(hash(person2))  # 2738403829
print(hash(person3))  # 2738403829  - последние два имеют одинаковый hash