# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на склад,
# нельзя использовать строковый тип данных.
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
        try:
            print(f'На склад отправилось {self.quant} принтера')
        except:
            print("Введенное значение должно быть числом!")



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