# class MyClass:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#     def __del__(self):
#         print(f'удалили {self}')
#
#
# obj1 = MyClass('obj1')
# del obj1  # удалили obj1

class MyClass:
    """Это документация класса MyClass."""

    def __init__(self, value):
        """Это документация конструктора."""
        self.value = value

    def get_value(self):
        """Это документация метода."""
        return self.value

print(MyClass.__doc__)            # Документация класса MyClass
print(MyClass.__init__.__doc__)   # Документация конструктора
print(MyClass.get_value.__doc__)  # Документация метода get_value

# help(MyClass)