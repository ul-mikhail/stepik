
def some_func(x, y):
    if y == 0:
        print('y = 0, на ноль делить нельзя')
    elif x == y:
        print('Это же одни и те же числа! понятно, что будет 1!  ')
    else:
        print(x/y)

def new_func(a, b):
    x = a+b
    print(x)
new_func(2, -5)