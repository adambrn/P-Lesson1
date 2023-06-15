def is_prime_number(number):
    if number == 2:
        return True
    if not number % 2:
        return False
    for i in range(3, int(number ** 0.5 + 1),2):
        if not number % i:
            return False
    return True

valid_input = False

while not valid_input:
    try:
        user_input = int(input("Введите число (от 2 до 100000): "))
        if user_input >= 2 and user_input <= 100000:
            valid_input = True
        else:
            print("Число должно быть от 2 до 100000. Повторите ввод.")
    except ValueError:
        print("Некорректный ввод. Повторите ввод числа.")

if is_prime_number(user_input):
    print("Число является простым.")
else:
    print("Число является составным.")
