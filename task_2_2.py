result_list =[]
j=int(input("Сколько элеентов массива предполагается ввести? "))
for i in range(j):
    result_list.append(input("Введите элемент "))

number = len(result_list)
if number%2 == 0:
    k = len(result_list)-1
else:
    k = len(result_list) - 2

for i in range(0, k, 2):
    a = result_list[i]
    result_list[i]=result_list[i+1]
    result_list[i+1] = a

print(result_list)
