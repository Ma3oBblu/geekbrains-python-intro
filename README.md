# Geekbrains.ru - Основы языка Python

Решение заданий по курсу [Видеокурс Основы языка Python](https://geekbrains.ru/chapters/6295)

## Урок #1
### Задание #1

Запросите от пользователя число, сохраните в переменную, прибавьте к числу 2 и выведите результат на экран. 

Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.

[Решение](https://github.com/Ma3oBblu/geekbrains-python-intro/blob/main/lesson1_1/main.py)

### Задание #2

Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 0, но меньше 10.

После того, как пользователь введет корректное число, возведите его в степень 2 и выведите на экран.

Например, пользователь вводит число 123, вы сообщаете ему, что число неверное, и говорите о диапазоне допустимых. 

И просите ввести заново.

Допустим, пользователь ввел 2, оно подходит. Возводим его в степень 2 и выводим 4.

[Решение](https://github.com/Ma3oBblu/geekbrains-python-intro/blob/main/lesson1_2/main.py)

### Задание #3
 
Создайте программу “Медицинская анкета”, где вы запросите у пользователя следующие данные: имя, фамилия, возраст и вес.

Выведите результат согласно которому:
- Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
- Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг
- Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
- Все остальные варианты вы можете обработать на ваш вкус и полет фантазии.

(Формула не соответствует реальной действительности и здесь используется только ради примера)

Примечание: при написание программы обратите внимание на условия в задаче и в вашем коде.  

Протестируйте программу несколько раз и убедитесь, что проверки срабатывают верно. 

В случае ошибок, уточните условия для той или иной ситуации.

```
Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!
```

[Решение](https://github.com/Ma3oBblu/geekbrains-python-intro/blob/main/lesson1_3/main.py)

## Урок #2
### Задание #1
Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.

Примечание. Списки создайте вручную, например так:
```
my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
```

[Решение](https://github.com/Ma3oBblu/geekbrains-python-intro/blob/main/lesson2_1/main.py)

### Задание #2
Дана дата в формате `dd.mm.yyyy`, например: `02.11.2013`. 

Ваша задача — вывести дату в текстовом виде, например: `второе ноября 2013 года`. 

Склонением пренебречь (2000 года, 2010 года)

[Решение](https://github.com/Ma3oBblu/geekbrains-python-intro/blob/main/lesson2_2/main.py)

### Задание #3
Дан список заполненный произвольными целыми числами.

Получите новый список, элементами которого будут только уникальные элементы исходного.
    
Примечание. Списки создайте вручную, например так:
`my_list_1 = [2, 2, 5, 12, 8, 2, 12]`

В этом случае ответ будет:
`[5, 8]`

[Решение](https://github.com/Ma3oBblu/geekbrains-python-intro/blob/main/lesson2_3/main.py)