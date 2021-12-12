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
id_dict = {0: 'Общественный транспорт',
           1: 'Социальная помощь',
           2: 'Образовательные учреждения',
           3: 'Спорт',
           4: 'Организация отдыха и оздоровления детей',
           5: 'Уборка снега',
           6: 'Реклама и граффити',
           7: 'Уличное освещение',
           8: 'Мусор',
           9: 'Дороги',
           10: 'Дворы',
           11: 'Парки'
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
for i in range(12):
    dict_main_words[i] = data[i].split()

dict_main_words_themes = {}
for i in range(len(data_themes)):
    dict_main_words_themes[i] = data_themes[i].split()

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
            for j in range(12):
                if morph.parse(text[i])[0].normal_form.lower() in dict_main_words[j]:
                    main_word = id_dict[j]
                    id_tem = j
                    for p in range(len(dict_main_words_themes)):
                        if morph.parse(text[i])[0].normal_form.lower() in dict_main_words_themes[p]:
                            theme = themes_id[p]
                        break
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