# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
#string_ = input('Введите строку из нескольких слов, разделённых пробелами: ')
st = 'Пользователь вводит строку из нескольких слов разделённых пробелами.'
st = st.split()
for id_, item in enumerate(st):
    print(f'{id_+1} -> {item[:10]}') if len(item) > 10 else print(f'{id_+1} -> {item}')