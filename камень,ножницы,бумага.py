import pyttsx3 # Импортируем модуль для озвучивания текста в речь
from random import randint

# Инициализируем движок для озвучивания текста в речь
engine = pyttsx3.init()

# Словарь для отображения значков
menu = {1: "🗿", 2: "✂️", 3: "📄", 4: "Выход"}

# Переменные для выбора пользователя и счета
choice = 0
user_score = 0
computer_score = 0


# Функция вывода меню
def show_menu():
    print("Выбери действие, введя число из списка ниже")
    for choice in range(1, 5):
        print(f"{choice}: {menu[choice]}")


# Функция для определения победителя раунда
def who_wins(user, computer):
    # Одинаковый выбор - ничья в раунде
    if user == computer:
        return "Ничья"
    # Набор условий, при которых побеждает пользователь
    elif (user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3 and computer == 1):
        return "Ты"
    # Любая другая ситуация - победа компьютера
    else:
        return "Компьютер"


# Функция словесного описания текущего исхода
def score_characteristic(user, computer):
    if user > computer:
        return "в твою пользу"
    elif computer > user:
        return "в пользу компьютера"
    else:
        return ". Пока ничья"


# Функция проверки пользовательского ввода
def input_and_check(current_choice):
    # Проверяем корректность ввода (изначально в переменную choice мы положили 0)
    while not (1 <= current_choice <= 4):
        show_menu()
        user_input = input()
        if user_input.isdigit() and 1 <= int(user_input) <= 4:
            current_choice = int(user_input)

    return current_choice


# Бесконечный цикл, каждая итерация - новый раунд
# Прервем его, если пользователь выберет "Выход"
while True:
    choice = input_and_check(choice)
    if choice == 4:
        # Выводим итоговый результат игры
        if user_score <= computer_score:
            print("Итог:\nКомпьютер выиграл! Было круто!")
            engine.say("Итог: Компьютер выиграл! Было круто!")
        elif user_score >= computer_score:
            print("Итог:\nТы выиграл! Было круто!")
            engine.say("Итог: Ты выиграл! Было круто!")
        else:
            print("Итог:\nНичья! Было круто!")
            engine.say("Итог: Ничья! Было круто!")

        # Озвучиваем итоговый результат игры
        engine.runAndWait()

        break

    # Случайный выбор компьютера от 1 до 3 включительно будет его ходом
    computer_choice = randint(1, 3)

    # Передаем в свою функцию выбор пользователя и компьютера, сохраняем возвращенное значение
    winner = who_wins(choice, computer_choice)

    # В зависимости от того, кто выиграл, увеличиваем счет
    if winner == "Ты":
        user_score += 1
    elif winner == "Компьютер":
        computer_score += 1

    # Выводим сообщение с исходом текущего раунда и общим счетом
    print(
        f"Ты - {menu[choice]}, компьютер - {menu[computer_choice]}. \nПобедитель раунда: {winner}. \nСчет "
        f"{user_score}:{computer_score} {score_characteristic(user_score, computer_score)}.\n")

    # правильное произношение иконок
    if menu[choice] == "🗿":
        icon_u = "Камень"
    if menu[choice] == "✂️":
        icon_u = "Ножницы"
    if menu[choice] == "📄":
        icon_u = "Бумага"
    if menu[computer_choice] == "🗿":
        icon_c = "Камень"
    if menu[computer_choice] == "✂️":
        icon_c = "Ножницы"
    if menu[computer_choice] == "📄":
        icon_c = "Бумага"

    # Озвучиваем результат текущего раунда
    engine.say(f"Ты - {icon_u}, компьютер - {icon_c}. Победитель раунда: {winner}. Счёт: "
               f"{user_score} {computer_score}")
    engine.runAndWait()

    # Обнуляем пользовательский выбор, чтобы заново его запросить на следующей итерации
    choice = 0
