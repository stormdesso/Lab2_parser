import json


def _print(value):
    print(value)
    pass


def _and(a, b):
    return a and b


def _or(a, b):
    return a or b


def _equal(a, b):
    return a == b


def _not(a):
    return not a


def _less(a, b):
    return a < b


def _more(a, b):
    return a > b


def read_json(file_name):
    # Opening JSON file
    f = open(file_name)

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    for i in data['dictionary']:
        print(i)
        if (list(dict(i).keys())[0] == 'print'):
            _print(list(dict(i).values())[0])

    # Closing file
    f.close()


def parse(element):
    if isinstance(element, list):  # список - функция
        res = []
        args = element[1:]  # считали все аргументы функции

        for arg in args:
            res.append(parse(arg))  # распарсили каждый аргумент

        fun_name = element[0]
        if fun_name in func_dict:
            return func_dict[fun_name](*res)  # распаковка аргументов функции
        else:
            print('команда не распознана: ', fun_name)
    else:
        return element


func_dict = {"print": _print, "and": _and, "or": _or, "equal": _equal, "not": _not, "less": _less, "more": _more}

input_commands = ["and", ["equal", 1, 2], True]

print(parse(input_commands))
