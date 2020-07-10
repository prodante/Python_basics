# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
def int_func(words):
    for let in words:
        if not ord(let) == 32 and not 97 <= ord(let) <= 122:
            print('Должны быть маленькие латинские буквы и пробел между ними.\n')
            words = input('Введите слова с пробелами (маленькие латинские буквы): \n')
            break
    words_list = words.split()
    for i in range(len(words_list)):
        print(words_list[i][0].upper() + words_list[i][1:], end=' ')

int_func(input('Введите слова с пробелами (маленькие латинские буквы): \n'))