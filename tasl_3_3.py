#Реализовать функцию my_func(),
#которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

arg1 = float(input("Введите первый аргумент: "))
arg2 = float(input("Введите второй аргумент: "))
arg3 = float(input("Введите третий аргумент: "))

def my_func(arg1, arg2, arg3):
    per=[arg1, arg2, arg3]
    m=per[0]
    sum = 0
    for i in range(len(per)):
        if(per[i]<m):
            m = per[i]

    for i in range(len(per)):
        if (per[i] != m):
            sum += per[i]


    return sum

print("Сумма = ", my_func(arg1, arg2, arg3))