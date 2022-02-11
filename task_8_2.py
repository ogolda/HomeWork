# Создайте собственный класс-исключение, обрабатывающий ситуацию
# деления на ноль. Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.

class devis():
    def __init__(self, num1, num2):
        self.num1 = float(num1)
        self.num2 = float(num2)

    def func(self):
        try:
            return('Результат деления %.2f' % (self.num1/self.num2))
        except ZeroDivisionError:
            return "На 0 делить нельзя!"


a = devis(2,0)
print(a.func())
b = devis(6,5)
print(b.func())