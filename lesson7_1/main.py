# Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
# Примечание: Списки фруктов создайте вручную в начале файла.
list1 = ['apple', 'orange', 'banana', 'mango']
list2 = ['pineapple', 'apple', 'banana']
result = [fruit for fruit in list1 if fruit in list1 and fruit in list2]
print(result)
