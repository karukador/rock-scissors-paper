import pyttsx3 #модуль для озвучивания текста
from random import randint

# Функция для озвучивания текста
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

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
    if user == computer:
        return "Ничья"
    elif (user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3 and computer == 1):
        return "Ты"
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
    while not (1 <= current_choice <= 4):
        show_menu()
        user_input = input()
        if user_input.isdigit() and 1 <= int(user_input) <= 4:
            current_choice = int(user_input)
    return current_choice

# Бесконечный цикл, каждая итерация - новый раунд
while True:
    choice = input_and_check(choice)
    if choice == 4:
        # Выводим итоговый результат игры
        if user_score < computer_score:
            result_text = "Итог: Компьютер выиграл! Было круто!"
            print("Итог:\nКомпьютер выиграл! Было круто!")
        elif user_score > computer_score:
            result_text = "Итог: Ты выиграл! Было круто!"
            print("Итог:\nТы выиграл! Было круто!")
        else:
            result_text = "Итог: Ничья! Было круто!"
            print("Итог:\nНичья! Было круто!")

        # Озвучиваем итоговый результат игры
        speak(result_text)
        break

    # Случайный выбор компьютера
    computer_choice = randint(1, 3)

    # Определяем победителя раунда
    winner = who_wins(choice, computer_choice)

    # Обновляем счет
    if winner == "Ты":
        user_score += 1
    elif winner == "Компьютер":
        computer_score += 1

    # Преобразуем иконки в слова
    icon_u = "Камень" if menu[choice] == "🗿" else "Ножницы" if menu[choice] == "✂️" else "Бумага"
    icon_c = "Камень" if menu[computer_choice] == "🗿" else "Ножницы" if menu[computer_choice] == "✂️" else "Бумага"

    # Формируем текст результата
    result_text = (f"Ты - {icon_u}, компьютер - {icon_c}. Победитель раунда: {winner}. "
                   f"Счёт: {user_score} : {computer_score}")

    # Выводим сообщение с исходом текущего раунда
    print(f"Ты - {menu[choice]}, компьютер - {menu[computer_choice]}.\n"
          f"Победитель раунда: {winner}.\n"
          f"Счёт {user_score}:{computer_score} {score_characteristic(user_score, computer_score)}.\n")

    # Озвучиваем результат текущего раунда
    speak(result_text)

    # Обнуляем пользовательский выбор
    choice = 0
