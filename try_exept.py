try:
    x = int(input())
    y = int(input())
    z = x / y
    f = open("file.txt")
except ZeroDivisionError:
    print('Деление на ноль')  # Вывод: Деление на ноль
except ValueError:
    print("Ошибка, переменная number не число")
except IOError:
    print("Ошибка открытия файла")


"""информация об исключении ZeroDivisionError будет сохранена в переменной p"""
try:
    x = 1 / 0
except Exception as p:
    print(f"{p}, {type(p)}")   # division by zero, <class 'ZeroDivisionError'>

"""исключение TypeError, и на консоль выводится информация об исключении и класс исключения.
также сохранится в переременную p"""
try:
    x = 1 / 'Vasya'
except Exception as p:
    print(f"{p}, {type(p)}")

# unsupported operand type(s) for /: 'int' and 'str', <class 'TypeError'>

def count(x, y):
    if y == 0:
        raise ZeroDivisionError('в функции count, y = 0, на ноль делить нельзя')
    return x / y

try:
    result = count(5, 0)
except ZeroDivisionError as zero:
    print(zero)  # в функции count, y = 0, на ноль делить нельзя
else:
    print(result)


"""оператор raise используется для генерации исключений"""
def some_func(x, y):
    if y == 0:
        raise ZeroDivisionError('в функции count, y = 0, на ноль делить нельзя')
    return x / y

try:
    result = some_func(5, 0)
except ZeroDivisionError as zero:
    print(zero)  # в функции count, y = 0, на ноль делить нельзя
else:
    print(result)