numbers = list(range(1, 10))

win_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def board():
    print('-------------')
    for i in range(3):
        print('|', numbers[0 + i * 3], '|', numbers[1 + i * 3], '|', numbers[2 + i * 3], '|')
    print('-------------')


def x_or_0(player_symbol):
    while True:
        value = input(f'Выберите клетку для "{player_symbol}": ')
        if not (value in list(str(123456789))):
            print('Выход за пределы игрового поля! Выберите цифру от "1" до "9" включительно!')
            continue
        value = int(value)
        if str(numbers[value - 1]) in 'X0':
            print('Эта клетка уже занята!')
            continue
        numbers[value - 1] = player_symbol
        break


def win():
    for i in win_combinations:
        if (numbers[i[0] - 1]) == (numbers[i[1] - 1]) == (numbers[i[2] - 1]):
            return numbers[i[0] - 1]
    else:
        return False


def main_func():
    counter = 0
    while True:
        board()
        if counter % 2 == 0:
            x_or_0("X")
        else:
            x_or_0("0")
        if counter > 3:
            winner = win()
            if winner:
                board()
                print(f'"{winner}" одержал победу! Ура!')
                break
        counter += 1
        if counter > 8:
            board()
            prin('Ничья!')
            break


main_func()
