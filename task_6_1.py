# Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.
import time

class TrafficLight:
    __color = ["red", "yellow", "green"]

    def running(self):
        i = 0
        for i in range(3):
            print(f'TrafficLight mode is { TrafficLight.__color[i]}')
            if i == 0:
                time.sleep(7)
            if i == 1:
                time.sleep(2)
            if i == 2:
                time.sleep(3)


tl = TrafficLight()
tl.running()





