# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.


with open('task_5_5.txt', 'w') as f:
    st = str(input("Введите числа "))
    f.writelines(st)

with open("task_5_5.txt") as f_op:
    for line in f_op:
        sl = line.split( )
s = 0
for i in range(len(sl)):
     s += float(sl[i])

print(f' Сумма чисел в файле = ', s)