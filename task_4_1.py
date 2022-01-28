# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта
# заработной платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv
script_name, vyr_ch, st_ch, prem = argv
def zp(vyr_ch,st_ch,prem):
    zp1 = float((vyr_ch * st_ch) + prem)
    return zp1

print("Имя скрипта: ", script_name)
print("Параметр 1: ", vyr_ch)
print("Параметр 2: ", st_ch)
print("Параметр 3: ", prem)
print(f'Заработная плата составляет: {zp(float(vyr_ch), float(st_ch), float(prem))}')



