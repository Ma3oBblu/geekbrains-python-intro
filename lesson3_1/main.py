# В этой игре человек загадывает число, а компьютер пытается его угадать.
# В начале игры человек загадывает число от 1 до 100 в уме или записывает его на листок бумаги.
# Компьютер начинает его отгадывать предлагая игроку варианты чисел.
# Если компьютер угадал число, игрок выбирает “победа”.
# Если компьютер назвал число меньше загаданного, игрок должен выбрать “загаданное число больше”.
# Если компьютер назвал число больше, игрок должен выбрать “загаданное число меньше”.
# Игра продолжается до тех пор пока компьютер не отгадает число.
import random

number = None
interval = {
    "min": 0,
    "max": 100000,
}
superNumber = random.randint(1, 100000)
print('super number is ==========> {} '.format(superNumber))
while number != superNumber:
    number = round((interval["max"] + interval["min"]) / 2)
    print('generated number is ====> {}'.format(number))
    if number == superNumber:
        print('winner with =====> {}'.format(number))
        break
    elif number > superNumber:
        interval["max"] = number
    else:
        interval["min"] = number
else:
    print("winner")
