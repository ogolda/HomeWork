# Представлен список чисел. Определите элементы списка, не имеющие повторений.
# Сформируйте итоговый массив чисел, соответствующих требованию. Элементы выведите в порядке их
# следования в исходном списке. Для выполнения задания обязательно используйте генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

from random import randint
my_list = []
n = int(input("Сколько значений должно быть в списке? "))
first = int(input ("Введите минимальное значение списка: "))
last = int(input ("Введите максимальное значение списка: "))
for i in range(n):
    my_list.append(randint(first, last))
print(f'Исходный массив: {my_list}')

# 1 способ
new_list = []
for i in range(n):
    per = my_list[i]
    k = 0
    for j in range(0, n):
        if my_list[j] == per:
            k = k + 1
    if k == 1:
        new_list.append(per)
    per = 0
print(f'Итоговый массив: {new_list}')

# 2 способ
new_list = [n for n in my_list if my_list.count(n) == 1]
print(f'Итоговый массив: {new_list}')