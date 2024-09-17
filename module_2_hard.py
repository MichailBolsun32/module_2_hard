while True:
    number_ = int(input('Введите любое чило от 3 до 20: '))
    if 3 <= number_ <= 20:
        result = []
        for i in range(1, number_):
            for j in range(i + 1, number_):
                if number_ % (i + j) == 0:
                    result.append(f'{i}{j}')
        break
    else:
        print('Вы ввели не верное число')

print(''.join(result))
