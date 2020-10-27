# Давайте усложним предыдущее задание. Измените сущности,
# добавив новый параметр - armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:
# Наносит урон. Это улучшенная версия функции из задачи 3.
# Вычисляет урон по отношению к броне.

# Примечание.
# Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа.

def attack(person1, person2):
    damage = get_damage(person1["damage"], person2["armor"])
    person2["health"] = person2["health"] - damage
    print(get_result(person1, person2, damage))


def get_damage(damage, armor):
    return round(damage / armor)


def get_result(person1, person2, damage):
    return 'игрок {} нанес урон {} игроку {}. осталось {} hp'.format(person1["name"], damage, person2["name"],
                                                                     person2["health"])


player_name = input('player name: ')
player = {
    "name": player_name,
    "health": 500,
    "damage": 50,
    "armor": 1.2,
}
enemy_name = input('enemy name: ')
enemy = {
    "name": enemy_name,
    "health": 500,
    "damage": 100,
    "armor": 1.2,
}

attack(enemy, player)
