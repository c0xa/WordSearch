import json
import copy


class Constants:  # class for constants values

    def __init__(self, extensibility):
        self.extensibility = extensibility / 180  # count matches for Ngram


class Vocabulary(object):  # class for vocabulary statistics

    def __init__(self):
        self.string = string
        self.len = len(string)

    def frequency(self):  # count the frequency of characters
        seq = list(self.string)
        count_dict = {}
        for elem in seq:
            if elem.isalpha():
                count_dict[elem] = count_dict.get(elem, 0) + 1
        for elem in count_dict:
            count_dict[elem] = count_dict.get(elem, 0) / self.len
        return sort_dict(count_dict)

    def repeat(self):  # count the repeat of characters
        i = 0
        count_bin = {}
        while i + 1 < self.len:
            if self.string[i:i + 1].isalpha():
                if self.string[i:i + 1] == self.string[i + 1:i + 2]:
                    count_bin[self.string[i:i + 2]] = count_bin.get(self.string[i:i + 2], 0) + 1
            i += 1
        return sort_dict(count_bin)

    def bi_gram(self):  # count the bi Gram
        i = 0
        count_bin = {}
        while i + 1 < self.len:
            if self.string[i:i + 2].isalpha():
                count_bin[self.string[i:i + 2]] = count_bin.get(self.string[i:i + 2], 0) + 1
            i += 1
        return selection(count_bin)

    def triple_gram(self):  # count the triple Gram
        i = 0
        count_triple = {}
        while i + 2 < self.len:
            if self.string[i:i + 3].isalpha():
                count_triple[self.string[i:i + 3]] = count_triple.get(self.string[i:i + 3], 0) + 1
            i += 1
        return selection(count_triple)

    def quad_gram(self):  # count the quad Gram
        i = 0
        count_quad = {}
        while i + 2 < self.len:
            if self.string[i:i + 4].isalpha():
                count_quad[self.string[i:i + 4]] = count_quad.get(self.string[i:i + 4], 0) + 1
            i += 1
        return selection(count_quad)

    def frequency_word(self):  # count repeated words
        count_word = {}
        count_word2 = {}
        seq = self.string.split(" ")
        for word in seq:
            if word.isalpha():
                count_word[word] = count_word.get(word, 0) + 1
        for elem in count_word:
            if count_word.get(elem, 0) > 1:
                count_word2[elem] = count_word.get(elem, 0)
        return sort_dict(count_word2)


def selection(dictionary):  # selection of unnecessary values
    dictionary2 = {}
    for elem in dictionary:
        if dictionary.get(elem, 0) > const.extensibility:
            dictionary2[elem] = dictionary.get(elem, 0)
    return sort_dict(dictionary2)


def sort_dict(dictionary2):  # sort values
    dict_sort = {}
    sorted_keys = sorted(dictionary2, key=dictionary2.get)
    for w in sorted_keys:
        dict_sort[w] = dictionary2[w]
    return dict_sort


def accordance_characters():  # the choice of symbols
    repeat = list(voc_repeat)
    frequency = list(voc_frequency)
    vocabulary_word = list(voc_word)
    if len(repeat) > 0:
        accordance[repeat[-1][0]] = 'н'
    if len(frequency) > 0:
        if vocabulary_word.count(frequency[-1]) == 1:
            accordance[frequency[-1]] = 'е'
        else:
            accordance[frequency[-1]] = 'о'
    flag_one = 1
    for elem in reversed(vocabulary_word):
        if len(elem) == 1:
            if flag_one == 1:
                flag_one = 2
                accordance[elem] = 'и'
            elif 0.040 < voc_frequency.get(elem, 0) < 0.05:
                accordance[elem] = 'с'
            elif 0.030 < voc_frequency.get(elem, 0) < 0.040:
                accordance[elem] = 'в'
            elif 0.026 < voc_frequency.get(elem, 0) < 0.030:
                accordance[elem] = 'к'
            elif 0.021 < voc_frequency.get(elem, 0) < 0.026:
                accordance[elem] = 'у'
            elif 0.001 < voc_frequency.get(elem, 0) < 0.021 and flag_one != 3:
                accordance[elem] = 'я'
                flag_one = 3
        if len(elem) == 3:
            if elem[0] == elem[2]:
                if voc_frequency.get(elem[0], 0) > 0.045:
                    accordance[elem[1]] = 'л'
                    accordance[elem[1]] = 'и'
                else:
                    accordance[elem[0]] = 'к'
                    accordance[elem[1]] = 'а'
    for elem in reversed(vocabulary_word):
        if len(elem) == 6:
            if elem[2] == elem[4] and voc_frequency.get(elem[2], 0) > 0.06:
                accordance[elem[0]] = 'с'
                accordance[elem[1]] = 'к'
                accordance[elem[3]] = 'з'
                accordance[elem[5]] = 'л'
    return accordance


if __name__ == "__main__":
    dict_for_one_pack = {}
    accordance = {}
    main = []
    f = open('input.txt', "r", encoding="utf-8")  # read input text
    string = f.read()
    pack = Vocabulary()
    const = Constants(pack.len)
    voc_frequency = pack.frequency()
    voc_repeat = pack.repeat()
    voc_triple_gram = pack.triple_gram()
    voc_bi_gram = pack.bi_gram()
    voc_quad_gram = pack.quad_gram()
    voc_word = pack.frequency_word()
    dict_for_one_pack["len"] = pack.len
    dict_for_one_pack["text"] = string
    dict_for_one_pack["keywords"] = voc_frequency
    dict_for_one_pack["Repeat"] = voc_repeat
    dict_for_one_pack["Binary"] = voc_bi_gram
    dict_for_one_pack["Triple"] = voc_triple_gram
    dict_for_one_pack["Quad"] = voc_quad_gram
    dict_for_one_pack["Frequency word"] = voc_word
    main.append(copy.copy(dict_for_one_pack))
    with open('output.json', 'w', encoding='utf-8') as file:  # write statistics to JSON
        json.dump(main, file, indent=2, ensure_ascii=False)
    accordance_characters()
    with open('accordance.json', 'w', encoding='utf-8') as file:   # write accordance between characters
        json.dump(accordance, file, indent=2, ensure_ascii=False)

    new_string = ""
    for elem in string:
        if accordance.get(elem, 0) != 0:
            new_string += accordance.get(elem, 0)
        else:
            new_string += elem
    fd = open('output.txt', 'w')
    fd.write(new_string + '\n')
    f.close()
    fd.close()
