import re, pymorphy2, csv

# from search import *

morph = pymorphy2.MorphAnalyzer()
main_word = ''
id_tem = ''
theme = ''
data = open('main_words.txt', encoding='utf-8').read().splitlines()
data_themes = open('main_words_themes.txt', encoding='utf-8').read().splitlines()
themes = open('themes.txt', encoding='utf-8').read().splitlines()
themes_id = open('themes id.txt', encoding='utf-8').read().splitlines()
file = []

# Словарь id
id_dict = {1: 'Общественный транспорт',
           2: 'Социальная помощь',
           3: 'Образовательные учреждения',
           4: 'Спорт',
           5: 'Организация отдыха и оздоровления детей',
           6: 'Уборка снега',
           7: 'Реклама и граффити',
           8: 'Уличное освещение',
           9: 'Мусор',
           10: 'Дороги',
           11: 'Дворы',
           12: 'Парки'
           }

# Словарь тем
dict_themes_id = {}
for i in range(1, len(themes_id) + 1):
    dict_themes_id[i] = themes_id[i - 1]

dict_themes = {}
for i in range(len(themes)):
    if themes[i].isdigit():
        a = int(themes[i])
    else:
        if a in dict_themes:
            dict_themes[a].append(themes[i])
        else:
            dict_themes[a] = [themes[i]]

# Словарь ключевых слов
dict_main_words = {}
for i in range(1, 13):
    dict_main_words[i] = data[i - 1].split()

dict_main_words_themes = {}
for i in range(len(data_themes)):
    if data_themes[i].isdigit():
        a = int(data_themes[i])
    else:
        if a in dict_main_words_themes:
            dict_main_words_themes[a].append(data_themes[i])
        else:
            dict_main_words_themes[a] = [data_themes[i]]
# Открываем csv файл
text = {}
with open('primer.csv', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    for row in reader:
        text[int(row['\ufeffid'])] = row['comment_text']

csvoutputfile = open('output.csv', 'a', encoding='utf8')


def search(text, main_word, id_tem, theme, file):
    comment = text
    text = re.split('\W', text)
    for i in range(len(text)):
        if text[i] != '' and len(text[i]) != 1:
            for j in range(1, 13):
                if morph.parse(text[i])[0].normal_form.lower() in dict_main_words[j]:
                    main_word = id_dict[j]
                    id_tem = j
    if id_tem != '' and main_word != '':
        for i in range(len(text)):
            for p in dict_main_words_themes[id_tem]:
                if morph.parse(text[i])[0].normal_form.lower() in p and \
                        len(morph.parse(text[i])[0].normal_form.lower()) > 1:
                    dict_main_words_themes[id_tem].index(p)
                    theme = dict_themes[id_tem][dict_main_words_themes[id_tem].index(p)]
    file.append({'cat_id': id_tem,
                 'cat_name': main_word,
                 'theme_name': theme,
                 'comment_text': comment})


for i in range(1, len(text) + 1):
    search(text[i], main_word, id_tem, theme, file)

with open('output.csv', 'w', newline='', encoding="utf8") as f:
    writer = csv.DictWriter(
        f, fieldnames=list(file[0].keys()),
        delimiter=';', quotechar='"')
    writer.writeheader()
    for d in file:
        writer.writerow(d)
