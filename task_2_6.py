#goods= [
#    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
#    (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."})
#]
kol = int(input("Сколько товаров вы хотите ввести? "))

goods = []
d=[]
d = dict.fromkeys(["название", "цена", "количество", "eд"])
print(d)
#ввод товаров
for i in range(kol):
    name = str(input("Введите наименование товара: "))
    price = float(input("Введите цену товара: "))
    quantity = int(input("Введите количество товара: "))
    ed = str(input("Введите единицу измерения: "))
    d["название"] = name
    d["цена"]=price
    d["количество"]=quantity
    d["eд"] = ed
    print(d)
    goods.append(d)

print(goods)

st = goods[0].keys()
key=[]
new_d=[]
for i in st:
    key.append(i)
print(key)

for i in key:
    a = []
    for j in range(len(goods)):
        per = goods[j][i]
        a.append(per)
    new_d.append(a)
print(new_d)

zipped = dict(zip(key, new_d))
print(zipped)