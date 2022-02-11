# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на склад,
# нельзя использовать строковый тип данных.
class sklad():
    def __init__(self):
        self.arr = {"printer": 0, "scaner": 0, "xerox": 0}

    def priem(self, name, quantity):
        self.quantity = quantity
        self.name = name
        try:
            if self.name == 'printer':
                self.arr["printer"] = int(self.arr.get("printer")) + self.quantity
            if self.name == 'scaner':
                self.arr["scaner"] = int(self.arr.get("scaner")) + self.quantity
            if self.name == 'xerox':
                self.arr["xerox"] = int(self.arr.get("xerox")) + self.quantity
            print(f'Был добавлен {self.name}  в количестве {self.quantity} шт. Актуальное состояние склада {self.arr}')
        except ValueError:
            print("Введены некорректные данные")
        except TypeError:
            print("Введены некорректные данные")

    def spisanie(self, name, quantity):
        self.quantity = quantity
        self.name = name

        try:
            if self.name == 'printer':
                self.arr["printer"] = int(self.arr.get("printer")) - quantity
            if self.name == 'scaner':
                self.arr["scaner"] = int(self.arr.get("scaner")) - quantity
            if self.name == 'xerox':
                self.arr["xerox"] = int(self.arr.get("xerox")) - quantity
            print(f'Был списан {self.name}  в количестве {quantity} шт. Актуальное состояние склада {self.arr}')
        except ValueError:
            print("Введены некорректные данные")
        except TypeError:
            print("Введены некорректные данные")


class tech():
    def __init__(self, price, color, weight):
        self.price = price
        self. color = color
        self.weight = weight

class printer(tech):
    def __init__(self, price, color, weight, speed):
        super().__init__(price, color, weight)
        self.speed = speed


class scaner(tech):
    def __init__(self, price, color, weight, lamp):
        super().__init__(price, color, weight)
        self.lamp = lamp

class xerox(tech):
    def __init__(self, price, color, weight, pages):
        super().__init__(price, color, weight)
        self.pages = pages

pr = printer(100, "white", 3.2, 16)
a = sklad()
a.priem("printer", 5)
a.priem("scaner", "r")

a.spisanie("printer", 2)