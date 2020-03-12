import numpy as np


# Параметр number - загаданное число


def game(number):
    predict = 0
    attempts_count = 0
    line = list(range(1, 101))
    l, r = 0, len(line) - 1

    while l <= r:
        middle = l + (r - l) // 2

        if line[middle] == number:
            attempts_count += 1
            predict = line[middle]
            break

        if line[middle] < number:
            attempts_count += 1
            l = middle + 1
            predict = line[l + (r - l) // 2]

        else:
            attempts_count += 1
            r = middle - 1
            predict = line[l + (r - l) // 2]

    print(f'Было загадано число {predict}. Отгадано за {attempts_count} попыток.')


# Тест
game(25)
game(15)
game(88)
game(37)
game(1)
game(50)
game(100)
game(61)
game(59)
game(33)
game(77)

# Результат
print('\n')
game(np.random.randint(1, 101))





