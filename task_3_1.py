#Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def dev(per1, per2):
    try:
        per1/per2
    except ZeroDivisionError:
        print("Division by zero")
        return 0
    return per1/per2

per1 = float(input("Введите делимое: "))
per2 = float(input("введите делитель: "))
print('%.2f' % dev(per1, per2))