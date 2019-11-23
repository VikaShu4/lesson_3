# Открыть текст

f = open('text.txt', 'r', encoding = 'utf-8')
text = f.read()
print(text)
f.close()

# №1 Методами строк очистить текст от знаков препинания.
# # Используемые в тексте знаки препинания: "«", "!", ".", ",", "—", "-", ";", "?", "»", "(", ")".

# 1 вариант, убирать по одному знаку:
textWithoutPunct = text.replace("«", " ")
print(textWithoutPunct)
textWithoutPunct = text.replace("!", " ")
print(textWithoutPunct)
# и т.п.
# 2 вариант, быстрый:
punct = "«!.,—;?»-()"
print(punct)
for i in punct:
    text = text.replace(i, " ")
print(text)

# №2 Cформировать list со словами
text_list = text.split()
print(text_list)

# №3  Привести все слова к нижнему регистру

text_list_map = list(map(lambda x:x.lower(), text_list))
print(text_list_map)

# №3 Получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте

text_dict = {}
for word in text_list_map:
    count = text_dict.get(word, 0)
    text_dict[word] = count + 1
print(text_dict)

# №4  Вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set)
# № 4.1

text_dict_list = list(text_dict.items())
text_dict_list.sort(key=lambda x: x[1], reverse=True)
print(text_dict_list [:5])

# №4.2

print(set(text_list_map), len(set(text_list_map)))

# № 5 Выполнить лемматизацию в пункте №2
# Из №3 взята переменная, включающая текст, состоящий из слов, отображенных нижним регистром

import pymorphy2
morph = pymorphy2.MorphAnalyzer()

text_lem = []
for i in text_list_map:
    text_lem.append(morph.parse(i)[0].normal_form)
print(text_lem)
