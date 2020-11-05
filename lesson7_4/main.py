# Написать функцию которая принимает на вход число от 1 до 100.
# Если число равно 13, функция поднимает исключительную ситуации ValueError
# иначе возвращает введенное число, возведенное в квадрат.
# Далее написать основной код программы. Пользователь вводит число.
# Введенное число передаем параметром в написанную функцию и печатаем результат, который вернула функция.
# Обработать возможность возникновения исключительной ситуации, которая поднимается внутри функции.

def check_number(number):
    if number == 13:
        raise ValueError
    else:
        return number ** 2


num = int(input('input number between 1 and 100: '))
try:
    print('result is', check_number(num))
except ValueError:
    print('ValueError: num is equal 13')
except Exception:
    print('unknown error')
