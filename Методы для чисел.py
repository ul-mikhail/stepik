# __add__      # используется для определения оператора сложения (+) между объектами
# __sub__      # используется для определения оператора вычитания (-) между объектами
# __mul__      # используется для определения оператора умножения (*) между объектами
# __pow__      # является специальным методом, который позволяет возвести в степень объект
# __truediv__  # используется для определения оператора деления (/) между объектами
# __abs__      # вызывается при использовании встроенной функции abs() для объекта

class Number:
    def __init__(self, number):
        self.number = number

    def  __add__ (self, other):
        if isinstance(other, Number):
            return self.number + other.number
        elif isinstance(other, int):
            return self.number + other

num1 = Number(100)
num2 = Number(200)
print(num1+num2)
print(num1+300)
print(num2+300)

class Number:
    def __init__(self, number):
        self.number = number

    def __sub__(self, other):
        return self.number - other    # экземпляр вычитает число

    def __rsub__(self, other):
        return other - self.number    # число вычитает экземпляр

num1 = Number(10)
result1 = 5 - num1       # вызовет __rsub__
result2 = num1 - 5       # вызовет __sub__
print(result1, result2)  # -5 5

class Number:
    def __init__(self, number):
        self.number = number

    def __mul__(self, other):
        return self.number * other  # экземпляр на число

    def __rmul__(self, other):
        return other * self.number  # число на экземпляр

num1 = Number(10)
result1 = 5 * num1       # вызовет __rmul__
result2 = num1 * 7       # вызовет __mul__
print(result1, result2)  # 50 70

class Number:
    def __init__(self, number):
        self.number = number

    def __pow__(self, power):
        if isinstance(power, int):
            return self.number ** power

    def __rpow__(self, power):
        if isinstance(self.number, int) and isinstance(power, int):
            return power ** self.number

num = Number(2)
print(num ** 3)  # 8
num = Number(2)
print(3 ** num)  # 9

class Number:
    def __init__(self, number):
        self.number = number

    def __truediv__(self, other):
        if isinstance(other, int) and other != 0:
            return self.number / other

    def __rtruediv__(self, other):
        if self.number != 0:
            return other / self.number

num1 = Number(50)
result1 = 100 / num1     # вызовет __rtruediv__
result2 = num1 / 5       # вызовет __truediv__
print(result1, result2)  # 2.0 10.0

class MyNumber:
    def __init__(self, number):
        self.number = number

    def __abs__(self):
        return abs(self.number)

my_number = MyNumber(-5)
print(abs(my_number))  # Output: 5