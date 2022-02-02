# Создать (не программно) текстовый файл со следующим содержимым:
# One - 1
# Two - 2
# Three - 3
# Four - 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

slov = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}
my_list = []
result = []
try:
    with open("task_5_4.txt") as f_op:
        for line in f_op:
            st = line.split(" - ")
            print(st)
            if st[0] in slov:
                el = slov[st[0]]
                result.append(el + " - " + st[1])
        print(result)
except IOError:
    print("Произошла ошибка ввода-вывода!")

try:
    with open('task_5_4_out.txt', 'w', encoding='utf-8') as f:
        f.writelines(result)
except IOError:
    print("Произошла ошибка ввода-вывода!")
