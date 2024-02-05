
def some_func(x, y):
    if y == 0:
        print('в функции count, y = 0, на ноль делить нельзя')
    elif x == y:
        print('Это же одни и те же числа! понятно, что будет 1!  ')
    else:
        print('Результат деления:', x/y)

some_func(0, 5)