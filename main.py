import sys, re, pymorphy2

morph = pymorphy2.MorphAnalyzer()
main_word = ''
data = open('main_words.txt', encoding='utf-8').read()

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

# Словарь ключевых слов
list_main_words = {0: data.split('\n')[0].split(),
                   1: data.split('\n')[1].split(),
                   2: data.split('\n')[2].split(),
                   3: data.split('\n')[3].split(),
                   4: data.split('\n')[4].split(),
                   5: data.split('\n')[5].split(),
                   6: data.split('\n')[6].split(),
                   7: data.split('\n')[7].split(),
                   8: data.split('\n')[8].split(),
                   9: data.split('\n')[9].split(),
                   10: data.split('\n')[10].split(),
                   11: data.split('\n')[11].split(),
                   }

# Считываем текст потоковым вводом и создаем список из слов
text = sys.stdin.read()
text = re.split('\W', text)

for i in range(len(text)):
    if text[i] != '' and len(text[i]) != 1:
        for j in range(12):
            if morph.parse(text[i])[0].normal_form.lower() in list_main_words[j]:
                main_word = id_dict[j]
                break

print(main_word)