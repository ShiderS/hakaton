import sys, re, pymorphy2, csv
from search import *

morph = pymorphy2.MorphAnalyzer()
main_word = ''
id1 = ''
data = open('main_words.txt', encoding='utf-8').read()
themes = open('themes.txt', encoding='utf-8').read()
themes_id = open('themes id.txt', encoding='utf-8').read()

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
for i in range(1, len(themes_id.split('\n')) + 1):
    dict_themes_id[i] = themes.split('\n')[i]
print(dict_themes_id)

dict_themes = {}
for i in range(len(themes.split('\n'))):
    if themes.split('\n')[i].isdigit():
        a = int(themes.split('\n')[i])
    else:
        if a in dict_themes:
            dict_themes[a].append(themes.split('\n')[i])
        else:
            dict_themes[a] = [themes.split('\n')[i]]
print(dict_themes)

# Словарь ключевых слов
dict_main_words = {}
for i in range(12):
    dict_main_words[i] = data.split('\n')[i].split()

# Считываем текст потоковым вводом и создаем список из слов
text = sys.stdin.read()
text = re.split('\W', text)

search(text, morph, dict_main_words, id_dict)