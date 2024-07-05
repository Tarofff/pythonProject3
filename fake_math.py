def divide():# объявляем функцию
    first = 5
    second = 0
    if second == 0:
        print("ОШИБКА")
    else:
        print(f'РЕЗУЛЬТАТ = {first / second}')
    return first, second
    print(divide())
divide()