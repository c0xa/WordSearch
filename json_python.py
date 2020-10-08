import json  # Подключили библиотеку

seq = map(str, input().split(';'))  # Чтение с консоли (потом переделать)

# Кортеж для слов
arry = ("сбор", "запись", "систематизация", "накопление", "хранение", "уточнение (обновление, изменение)", "извлечение",
        "использование", "передача (распространение, предоставление, доступ)", "удаление")
countDict = {}

for elem in seq:    # Каждое слово перебираем
    elem = elem.strip()   # убираем пробелы
    if arry.count(elem):    # сравниваем с кортежем
        countDict[elem] = countDict.get(elem, 0) + 1  # cчитаем кол-во слов


y = json.dumps(countDict, ensure_ascii=False)  # в формат json
print(y)   # выводим для проверки

with open('test_file.json', 'w', encoding='utf-8') as file:   # открываем файл и записываем
    json.dump(y, file, indent=2, ensure_ascii=False)

# для проверки
with open('test_file.json', 'r', encoding='utf-8') as f:  # открыли файл
    text = json.load(f)  # поместили все из файла в переменную
    print(text)  # вывели результат на экран


'''''
for txt in text['Vocabulary']:  # создали цикл, который будет работать построчно
    print(txt['запись'], '- ', txt['data'])  # и выводим на экран все, что в значении ключей name и salary/'''