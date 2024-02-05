
class MyList:
    def __init__(self):
        self.data = [1, 2, 3, 4, 5]

    def __getitem__(self, item):
        return self.data[item]

my_list = MyList()
print(my_list[2])  # Выводит: 3

class MyList:
    def __init__(self):
        self.data = [1, 2, 3, 4, 5]

    def __getitem__(self, item):
        return self.data[item]

my_list = MyList()
print(my_list[2])  # Выводит: 3

class MyDict:
    def __init__(self):
        self.data = {}

    def __setitem__(self, key, value):
        self.data[key] = value

my_dict = MyDict()
my_dict['name'] = 'John'
print(my_dict.data)  # Выводит: {'name': 'John'}

class MyList:
    def __init__(self):
        self.data = [1, 2, 3, 4, 5]

    def __delitem__(self, index):
        del self.data[index]

my_list = MyList()
del my_list[2]
print(my_list.data)  # Выводит: [1, 2, 4, 5]

class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

my_list = MyList([1, 2, 3, 4, 5])
print(len(my_list))  # Output: 5


"""используется, когда нужен дополнительный функционал, например с каждой итерацией
 выводить сообщение, или делать подсчёты и т.д"""
class MyIterator:
    def __init__(self, data):
        self.data = data  # итерируемый объект
        self.index = 0    # счётчик итераций

    def __iter__(self):
        return self

    def __next__(self):   # код ниже, запускается при каждой итерации
        if self.index >= len(self.data):
            raise StopIteration
        item = self.data[self.index]
        self.index += 1
        return f'новая итерация {item}'

my_iterator = MyIterator([1, 2, 3, 4, 5])
for i in my_iterator:
    print(i)

"""Тоже самое, но тут список уже в самом классе.  используется в самых простых ситуациях,
 когда не нужен дополнительный функционал. Просто указываете в __iter__ какой объект
  использовать, когда в цикле проходите по экземпляру."""
class MyList:
    def __init__(self):
        self.data = [1, 2, 3, 4, 5]

    def __iter__(self):
        return iter(self.data)

my_list = MyList()
for item in my_list:
    print(item)