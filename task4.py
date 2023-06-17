from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
MAX_ATTEMPTS = 10


target_number = randint(LOWER_LIMIT, UPPER_LIMIT)
attempts = 0

while attempts < MAX_ATTEMPTS:
    user_guess = int(input("Введите ваше предположение: "))

    if user_guess < target_number:
        print("Загаданное число больше.")
    elif user_guess > target_number:
        print("Загаданное число меньше.")
    else:
        print("Вы угадали число!")
        break
    attempts += 1

if attempts == MAX_ATTEMPTS:
    print("К сожалению, вы исчерпали все попытки. Загаданное число было:", target_number)

