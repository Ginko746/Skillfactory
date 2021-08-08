import numpy as np

number = np.random.randint(1, 101)  # загадываем случайное число от 1 до 100
print("Загадано число от 1 до 100")


def game_core_v3(number):  # принимаем загаданное число и возвращаем количество попыток угадывания
    count = 1  # количество попыток
    predict = 50  # начальное предположение
    while number != predict:  # отгадываем уменьшая возможный дипазон в 2 раза
        step = round(51/2**count)  # шаг в меньший диапазон
        count += 1
        if number > predict:
            predict += step
        elif number < predict:
            predict -= step
    return count  # выход из цикла, если угадали


def score_game(game_core):  # среднее количество попыток за 1000 игр
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core_v3)
