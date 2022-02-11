# Разработайте методы, которые отвечают за приём оргтехники на склад и передачу
# в определённое подразделение компании. Для хранения данных о наименовании и
# количестве единиц оргтехники, а также других данных, можно использовать любую
# подходящую структуру (например, словарь).

class tech():
    def __init__(self, price, color, weight):
        self.price = price
        self. color = color
        self.weight = weight

class printer(tech):
    def __init__(self, price, color, weight, speed):
        super().__init__(price, color, weight)
        self.speed = speed

    def to_store(self, quant):
        self.quant = quant
        print(f'На склад отправилось {self.quant} принтера')



class scaner(tech):
    def __init__(self, price, color, weight, lamp):
        super().__init__(price, color, weight)
        self.lamp = lamp

class xerox(tech):
    def __init__(self, price, color, weight, pages):
        super().__init__(price, color, weight)
        self.pages = pages

pr = printer(100, "white", 3.2, 16)
pr.to_store(2)