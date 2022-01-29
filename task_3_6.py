# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и
# возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
def int_func(st):
    return st.title()

st = str(input("Введите строку: "))
print(int_func(st))

