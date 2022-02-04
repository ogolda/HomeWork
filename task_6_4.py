# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
# (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
    #должны сообщать, что машина поехала,
        return('Машина поехала')

    def stop(self):
    # остановилась,
        return('Машина остановилась')

    def turn_right(direction):
    #  повернула (куда);
        return('Машина повернула направо')

    def turn_left(direction):
        #  повернула (куда);
        return('Машина повернула налево')

    def show_speed(self):
    #показывать текущую скорость автомобиля
        return('Текущая скорость ' + self.speed)

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
    #При значении скорости свыше 60 должно выводиться сообщение о превышении скорости
        if self.speed > 60:
            return('Скорость превышена!')
        else:
            return('Текущая скорость составляет ' + str(self.speed))

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
    #При значении скорости свыше 40 должно выводиться сообщение о превышении скорости
        if self.speed > 40:
            return('Скорость превышена!')
        else:
            return('Текущая скорость составляет ' + str(self.speed))

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def police(self):
        return('Это полицейская машина')

a = TownCar(70, 'white', 'Toyota', False)
print(a.show_speed())
a = WorkCar(30, 'white', 'Toyota', False)
print(a.show_speed())
a = PoliceCar(70, 'white', 'Toyota', True)
print(a.police())