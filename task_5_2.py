# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.
i = 0
i_len = 0
with open("task_5_1.txt") as f_op:
    for line in f_op:
        i += 1
        st = line
        i_len = len(st.split( ))
        print(f'В {i} строке {i_len} слов')
        i_len = 0
