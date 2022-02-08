# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod
class cloths(ABC):
    @abstractmethod
    def sq(self):
        #empty body
        pass

class coat(cloths):
    def sq(self):
        #empty body
        pass
class jacket(cloths):
    def sq(self):
        #empty body
        pass


class my_coat(coat):
    def __init__(self, v):
        self.v = v
    @property
    def sq(self):
        return '%.2f' % (self.v/6.5 + 0.5)

class my_jacket(coat):
    def __init__(self, h):
        self.h = h

    @property
    def sq(self):
        return'%.2f' % (self.h*2 + 0.3)

c = my_coat(3)
j = my_jacket(2)
a = c.sq
b = j.sq
print(f'Площадь ткани для пошива пальто составляет:  {c.sq} м.кв.')
print(f'Площадь ткани для пошива костюма составляет:  { j.sq} м.кв.')
itog = float(a) + float(b)
print(f'Общая площадь ткани составляет: {itog} м.кв.')



# @property
#def my_method(self):
#    return f"Общая площаль ткани составляет: ", self.size


