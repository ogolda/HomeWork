str=str(input("Введите строку "))

str_list = str.split()

str_len = len(str.split())
for i in range(str_len):
    if len(str_list[i]) < 10:
        print(i+1, "слово: ", str_list[i])
    else:
        s=str_list[i]
        print(i+1, "слово: ", s[0:10])
