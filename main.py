import re, pymorphy2, csv
# from search import *


class Main:
    def __init__(self, file_name):
        self.morph = pymorphy2.MorphAnalyzer()
        self.main_word = ''
        self.id_tem = ''
        self.theme = ''
        self.data = open('files/main_words.txt', encoding='utf-8').read().splitlines()
        self.data_themes = open('files/main_words_themes.txt', encoding='utf-8').read().splitlines()
        self.themes = open('files/themes.txt', encoding='utf-8').read().splitlines()
        self.themes_id = open('files/themes id.txt', encoding='utf-8').read().splitlines()
        self.file = []

        # Словарь id
        self.id_dict = {1: 'Общественный транспорт',
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
        self.dict_themes_id = {}
        for i in range(1, len(self.themes_id) + 1):
            self.dict_themes_id[i] = self.themes_id[i - 1]

        self.dict_themes = {}
        for i in range(len(self.themes)):
            if self.themes[i].isdigit():
                a = int(self.themes[i])
            else:
                if a in self.dict_themes:
                    self.dict_themes[a].append(self.themes[i])
                else:
                    self.dict_themes[a] = [self.themes[i]]

        # Словарь ключевых слов
        self.dict_main_words = {}
        for i in range(1, 13):
            self.dict_main_words[i] = self.data[i - 1].split()

        self.dict_main_words_themes = {}
        for i in range(len(self.data_themes)):
            if self.data_themes[i].isdigit():
                a = int(self.data_themes[i])
            else:
                if a in self.dict_main_words_themes:
                    self.dict_main_words_themes[a].append(self.data_themes[i])
                else:
                    self.dict_main_words_themes[a] = [self.data_themes[i]]
        # Открываем csv файл
        self.text = {}
        with open(f'static/saved_files/{file_name}', encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
            for row in reader:
                self.text[int(row['\ufeffid'])] = row['comment_text']

        self.csvoutputfile = open('output.csv', 'a', encoding='utf8')
        self.creature_csv()

    def creature_csv(self):
        for self.i in range(1, len(self.text) + 1):
            self.search()

        with open(f'static/saved_files/output.csv', 'w', newline='', encoding="utf8") as f:
            writer = csv.DictWriter(
                f, fieldnames=list(self.file[0].keys()),
                delimiter=';', quotechar='"')
            writer.writeheader()
            for d in self.file:
                writer.writerow(d)
        return self.file

    def search(self):
        comment = self.text[self.i]
        text = re.split('\W', self.text[self.i])
        for i in range(len(text)):
            if text[i] != '' and len(text[i]) != 1:
                for j in range(1, 13):
                    if self.morph.parse(text[i])[0].normal_form.lower() in self.dict_main_words[j]:
                        self.main_word = self.id_dict[j]
                        self.id_tem = j
        if self.id_tem != '' and self.main_word != '':
            for i in range(len(text)):
                for p in self.dict_main_words_themes[self.id_tem]:
                    if self.morph.parse(text[i])[0].normal_form.lower() in p and \
                            len(self.morph.parse(text[i])[0].normal_form.lower()) > 1:
                        self.dict_main_words_themes[self.id_tem].index(p)
                        self.theme = self.dict_themes[self.id_tem][self.dict_main_words_themes[self.id_tem].index(p)]
        self.file.append({'cat_id': self.id_tem,
                     'cat_name': self.main_word,
                     'theme_name': self.theme,
                     'comment_text': comment})