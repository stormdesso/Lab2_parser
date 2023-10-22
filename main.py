import json
import custom_parser


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


def fact_exist(fact_name):
    return fact_name in fact_base


def fact_not_exist(fact_name):
    return not fact_exist(fact_name)


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


def evaluate_rules(rules):
    for rule in rules:
        if parse(rule[0]):  # проверка условия у правила
            if isinstance(rule[1][0], list):  # список функций
                for action in rule[1]:
                    parse(action)
            else:
                parse(rule[1])


def determinate_fact_base():
    global fact_base  # факт:   значение

    fact_base = {}
    fact_base["test_fact2"] = "yes"
    pass


def determinate_function_list():
    global func_dict

    func_dict = {
        "print": _print,
        "and": _and,
        "or": _or,
        "equal": _equal,
        "not": _not,
        "less": _less,
        "more": _more,
        "fact_exist": fact_exist,
        "fact_not_exist": fact_not_exist,
    }
    pass


def initialize():
    determinate_fact_base()  # заполнил базу знаний
    determinate_function_list()  # определил список функций
    pass


def run():
    rules_list = custom_parser.parse_json_file("rules.json")
    evaluate_rules(rules_list)
    pass


if __name__ == "__main__":
    initialize()
    run()
