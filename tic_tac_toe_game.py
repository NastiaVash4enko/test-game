game_greeting = 'Добро пожаловать в игру "Крестики-Нолики"!'
print(game_greeting)

rules_game = "Правила игры таковы." \
             " Игроки по очереди ставят на свободные клетки поля 3х3 знаки" \
             " (один всегда крестики, другой всегда нолики).\n" \
             "Первый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или диагонали, выигрывает."

print(rules_game)


name_1 = input("Введите имя первого игрока")
name_2 = input("Введите имя второго игрока")
print(f'Добрый день,{name_1} и {name_2}!')
print("Первый ход делает игрок, ставящий крестик")

field = [['-'] * 3 for _ in range(3)]


def game_field(i):
    print('  0 1 2')
    for i in range(len(field)):
        print(str(i) + " " + " ".join(field[i]))


def user_input(f) -> object:
    global x, y
    while True:
        place = input(
            "Ваш ход, введите, пожалуйста, желаемые координаты: ").split()
        if len(place) != 2:
            print("Введите, пожалуйста, только две координаты через пробел")
            continue
        if not (place[0].isdigit() and place[1].isdigit()):
            print("Введите, пожалуйста, только числа")
            continue
        x, y = map(int, place)
        if not (0 <= x < 3 and 0 <= y < 3):
            print('Введенные координаты выходят за пределы поля, '
                  'введите, пожалуйста, координаты, соотвествующие полю игры "Крестики-нолики" ')
            continue
        if f[x][y] != "-":
            print(
                "Клетка уже занята, введите, пожалуйста другие координаты, чтобы продолжить игру")
            continue
        break
    return x, y


def win_1(f, user):
    f_list = []
    for L in f:
        f_list += L
    positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                 [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    indices = set([i for i, x in enumerate(f_list) if x == user])
    for p in positions:
        if len(indices.intersection(set(p))) == 3:
            return True
    # Было:
    #     return False
    # Стало:
    return False


count = 0
while True:
    if count == 9:
        print("Ничья")
        break
    if count % 2 == 0:
        users = 'Х'
    else:
        users = '0'
    game_field(field)
    x, y = user_input(field)
    field[x][y] = users
    if win_1(field, users):
        print(f"Поздравляю, выйграл {users}")
        game_field(field)
        break
    count += 1

print("Hello World!")
