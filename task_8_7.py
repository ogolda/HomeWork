# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, cel, mnim):
        self.cel = cel
        self.mnim = mnim

    def __add__(self, other):
        print(f'Сумма n1 и n2 равна')
        return f'z = {self.cel + other.cel} + {self.mnim + other.mnim} * i'

    def __mul__(self, other):
        print(f'Произведение n1 и n2 равно')
        return f'z = {(self.cel * other.cel - self.mnim * other.mnim)} + {self.cel * other.mnim + other.cel * self.mnim} * i'

    def __str__(self):
        return f'z = {self.cel} + {self.mnim} * i'


n1 = ComplexNumber(2, 3)
n2 = ComplexNumber(4, 5)
print(n1)
print(n1 + n2)
print(n1 * n2)