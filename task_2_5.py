my_list = [7, 5, 3, 3, 2]
number = int(input("Введите новое значение "))
k = 1
flag = False
list_len = len(my_list)
if my_list[0]<number:
    my_list.insert(0, number)
    flag = True

if flag == False:
    for i in range(len(my_list)-1):
        if my_list[i] >= number:
            if my_list[i+1] < number:
                print(my_list[i])
                k = int(i+1)
            else:
                k = len(my_list)
    my_list.insert(k, number)
print(my_list)
