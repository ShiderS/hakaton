import re


def search(text, morph, dict_main_words, id_dict, dict_main_words_themes, data_themes):
    text = re.split('\W', text)
    for i in range(len(text)):
        if text[i] != '' and len(text[i]) != 1:
            for j in range(12):
                if morph.parse(text[i])[0].normal_form.lower() in dict_main_words[j]:
                    main_word = id_dict[j]
                    id_tem = j
                    for p in range(len(dict_main_words_themes)):
                        if morph.parse(text[i])[0].normal_form.lower() in dict_main_words_themes[j]:
                            theme = data_themes[p]
                        break
    return id_tem, main_word, theme
