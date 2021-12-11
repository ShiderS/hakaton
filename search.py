def search(text, morph, dict_main_words, id_dict):
    for i in range(len(text)):
        if text[i] != '' and len(text[i]) != 1:
            for j in range(12):
                if morph.parse(text[i])[0].normal_form.lower() in dict_main_words[j]:
                    main_word = id_dict[j]
                    id1 = j
                    break
    return id1, main_word
