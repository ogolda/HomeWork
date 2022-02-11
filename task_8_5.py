# Разработайте методы, которые отвечают за приём оргтехники на склад и передачу
# в определённое подразделение компании. Для хранения данных о наименовании и
# количестве единиц оргтехники, а также других данных, можно использовать любую
# подходящую структуру (например, словарь).
class sklad():
    def __init__(self):
        self.arr = {"printer": 3, "scaner": 0, "xerox": 0}

    def priem(self, name, quantity):
        self.name = name
        self.quantity = int(quantity)
        if self.name == 'printer':
            self.arr["printer"] = int(self.arr.get("printer")) + self.quantity
        if self.name == 'scaner':
            self.arr["scaner"] = int(self.arr.get("scaner")) + self.quantity
        if self.name == 'xerox':
            self.arr["xerox"] = int(self.arr.get("xerox")) + self.quantity
        print(f'Был добавлен {self.name}  в количестве {self.quantity} шт. Актуальное состояние склада {self.arr}')

    def spisanie(self, name, quantity):
        self.name = name
        self.quantity = int(quantity)
        if self.name == 'printer':
            self.arr["printer"] = int(self.arr.get("printer")) - self.quantity
        if self.name == 'scaner':
            self.arr["scaner"] = int(self.arr.get("scaner")) - self.quantity
        if self.name == 'xerox':
            self.arr["xerox"] = int(self.arr.get("xerox")) - self.quantity
        print(f'Был списан {self.name}  в количестве {self.quantity} шт. Актуальное состояние склада {self.arr}')

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
a.priem("printer", 4)
a.spisanie("printer", 2)