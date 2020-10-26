# Дан список заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут только уникальные элементы исходного.
# Примечание. Списки создайте вручную, например так:
# my_list_1 = [2, 2, 5, 12, 8, 2, 12]
# В этом случае ответ будет:
# [5, 8]

my_list_1 = [2, 2, 5, 12, 8, 2, 12]
numbers_dict = {}
unique_list = []
for number in my_list_1:
    if number in numbers_dict.keys():
        numbers_dict[number] += 1
    else:
        numbers_dict[number] = 1

for key, value in numbers_dict.items():
    if value == 1:
        unique_list.append(key)

print(unique_list)
