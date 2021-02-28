import json  # Подключили библиотеку
import copy

class Constants():

    def __init__(self, extensibility):
        self.extensibility = extensibility / 180

class Vocabulary(object):

    def __init__(self, string):
        self.string = string
        self.len = len(string)

    def frequency(self):
        seq = list(self.string)
        countDict = {}
        sorted_dict = {}
        for elem in seq:
            if elem.isalpha():
                countDict[elem] = countDict.get(elem, 0) + 1
        for elem in countDict:
            countDict[elem] = countDict.get(elem, 0) / self.len
        sorted_keys = sorted(countDict, key=countDict.get)
        for w in sorted_keys:
            sorted_dict[w] = countDict[w]
        return sorted_dict

    def repeat(self):
        i = 0
        countBin = {}
        countBinSort = {}
        while i + 1 < self.len:
            if self.string[i:i + 1].isalpha():
                if (self.string[i:i + 1] == self.string[i + 1:i + 2]):
                    countBin[self.string[i:i + 2]] = countBin.get(self.string[i:i + 2], 0) + 1
            i += 1
        sorted_keys = sorted(countBin, key=countBin.get)
        for w in sorted_keys:
            countBinSort[w] = countBin[w]
        return countBinSort

    def biGram(self):
        i = 0
        countBin = {}
        countBin2 = {}
        countBinSort = {}
        while i + 1 < self.len:
            if self.string[i:i + 2].isalpha():
                countBin[self.string[i:i + 2]] = countBin.get(self.string[i:i + 2], 0) + 1
            i += 1
        for elem in countBin:
            if countBin.get(elem, 0) > const.extensibility:
                countBin2[elem] = countBin.get(elem, 0)
        sorted_keys = sorted(countBin2, key=countBin2.get)
        for w in sorted_keys:
            countBinSort[w] = countBin2[w]
        return countBinSort

    def tripleGram(self):
        i = 0
        countTriple = {}
        countTriple2 = {}
        countTripleSort = {}
        while i + 2 < self.len:
            if self.string[i:i + 3].isalpha():
                countTriple[self.string[i:i + 3]] = countTriple.get(self.string[i:i + 3], 0) + 1
            i += 1
        for elem in countTriple:
            if countTriple.get(elem, 0) > const.extensibility:
                countTriple2[elem] = countTriple.get(elem, 0)
        sorted_keys = sorted(countTriple2, key=countTriple2.get)
        for w in sorted_keys:
            countTripleSort[w] = countTriple2[w]
        return countTripleSort

    def quadGram(self):
        i = 0
        countQuad = {}
        countQuad2 = {}
        countQuadSort = {}
        while i + 2 < self.len:
            if self.string[i:i + 4].isalpha():
                countQuad[self.string[i:i + 4]] = countQuad.get(self.string[i:i + 4], 0) + 1
            i += 1
        for elem in countQuad:
            if countQuad.get(elem, 0) > const.extensibility:
                countQuad2[elem] = countQuad.get(elem, 0)
        sorted_keys = sorted(countQuad2, key=countQuad2.get)
        for w in sorted_keys:
            countQuadSort[w] = countQuad2[w]
        return countQuadSort

    def frequencyWord(self):
        countWord = {}
        countWord2 = {}
        countWordSort = {}
        seq = self.string.split(" ")
        for word in seq:
            if word.isalpha():
                countWord[word] = countWord.get(word, 0) + 1
        for elem in countWord:
            if countWord.get(elem, 0) > 2:
                countWord2[elem] = countWord.get(elem, 0)
        sorted_keys = sorted(countWord2, key=countWord2.get)
        for w in sorted_keys:
            countWordSort[w] = countWord2[w]
        return countWordSort

if __name__ == "__main__":
    dictForOnePack = {}
    accordance = {}
    main = []
    f = open('input.txt', "r", encoding="utf-8")
    string = f.read()
    pack = Vocabulary(string)
    const = Constants(pack.len)
    vocFrequency = pack.frequency()
    vocRepeat = pack.repeat()
    vocTripleGram = pack.tripleGram()
    vocBiGram = pack.biGram()
    vocQuadGram = pack.quadGram()
    vocWord = pack.frequencyWord()
    dictForOnePack["len"] = pack.len
    dictForOnePack["text"] = string
    dictForOnePack["keywords"] = vocFrequency
    dictForOnePack["Repeat"] = vocRepeat
    dictForOnePack["Binary"] = vocBiGram
    dictForOnePack["Triple"] = vocTripleGram
    dictForOnePack["Quad"] = vocQuadGram
    dictForOnePack["Frequency word"] = vocWord
    main.append(copy.copy(dictForOnePack))
    with open('output.json', 'w', encoding='utf-8') as file:   # открываем файл и записываем
        json.dump(main, file, indent=2, ensure_ascii=False)
    repeat = list(vocRepeat)
    if len(repeat) > 1:
        accordance[repeat[-1][0]] = 'н'
    if len(repeat) > 2:
        accordance[repeat[-2][0]] = 'о'
    with open('accordance.json', 'w', encoding='utf-8') as file:   # открываем файл и записываем
        json.dump(accordance, file, indent=2, ensure_ascii=False)

