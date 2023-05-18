# Дана строка состоящая из слов, все слова разделены ровно одним пробелом. Знаки препинания отсутствуют.
# Найдите первое слово, начинающееся на букву "б"
# если слова на эту букву нет, выведите "слов на б нет"
#text = "Скоро лето"
#text = "Будет лето"
text = "Лето будет"

start_word = text.lower().find(" б") + 1
if text.find(" ", start_word) == -1:
    end_word = len(text)
else:
    end_word = text.find(" ", start_word + 1)

if text[0].lower() == 'б':
    print(text[0:text.find(" ")])
elif text[text.find(" б") + 1].lower() == 'б':
    print(text[start_word:end_word])
else:
    print("слов на б нет")
