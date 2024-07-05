from math import inf
def divide():# объявляем функцию
    first = 4
    second = 0
    if second == 0:
        return inf
    else:
        print(f'РЕЗУЛЬТАТ = {first / second}')
    return first, second, inf
    print(divide())
divide()