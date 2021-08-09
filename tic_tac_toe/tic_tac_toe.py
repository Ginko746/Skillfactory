print("Давай сыграем в крестики-нолики!!!")
print("")
print("Первый Игрок ходит Х")
print("Второй Игрок ходит О")
print("")
print("Для того чтобы сделать ход")
print("необходимо ввести через пробел")
print("в начале номер строки, затем номер столбца")
print("")

field = [[" "] * 3 for i in range(3)]  # задаем переменную нашего поля
count = 0  # счетчик ходов
while True:  # Начинаем цикл игры
    count += 1

    def show():  # красиво выводим наше поле на экран
        print()
        print("    | 0 | 1 | 2 | ")
        print("  --------------- ")
        for i, row in enumerate(field):
            row_str = f"  {i} | {' | '.join(row)} | "
            print(row_str)
            print("  --------------- ")
        print()
    show()

    if count % 2 == 1:
        print("Ход первого игрока!")
    else:
        print("Ход второго игрока!")


    def ask():  # просим игрока сделать ход
        while True:
            cords = input("         Выбирай клетку: ").split()

            if len(cords) != 2:  # Если введено не 2 координаты
                print("Введите через пробел номер строки и столбца!")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):  # Если ввели не числа
                print("Введите числа!")
                continue

            x, y = int(x), int(y)

            if 0 > x or x > 2 or 0 > y or y > 2:  # Если ввели не верные координаты
                print("Введите значения от 0 до 2!")
                continue

            if field[x][y] != " ":  # Если выбрали занятую клетку
                print("Сюда ходить нельзя!")
                continue

            return x, y

    x, y = ask()

    if count % 2 == 1:  # Первый игрок ставит Х, а второй О
        field[x][y] = "X"
    else:
        field[x][y] = "0"


    def check_win():  # Проверяем достигнуты ли победные условия
        win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),  # Победные варианты
                    ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                    ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
        for cord in win_cord:
            symbols = []
            for c in cord:
                symbols.append(field[c[0]][c[1]])
            if symbols == ["X", "X", "X"]:
                print("Выиграл Первый игрок!")
                return True
            if symbols == ["0", "0", "0"]:
                print("Выиграл Второй игрок!")
                return True
        return False
    if check_win():  # Если достигнуто победное условие заканчиваем цикл игры
        break

    if count == 9:  # Если число ходов достигло 9 значит сыграли вничью
        print("УРА, Победила Дружба!!!")
        break
