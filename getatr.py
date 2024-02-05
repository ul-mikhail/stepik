class Person:
    def __init__(self):
        self.attributes = {"name": "John", "age": 30}

    def __getattr__(self, name):
        if name in self.attributes:
            return self.attributes[name]
        else:
            return "Атрибут не найден"

person = Person()
print(person.name)   # Вывод: John
print(person.age)    # Вывод: 30
print(person.height) # Вывод: Атрибут не найден