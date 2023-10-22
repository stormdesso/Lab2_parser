import json


def parse_json_file(path):
    with open(path, 'r') as f:
        raw_rules = json.load(f)
        input_rules = []

        for raw_rule in raw_rules['rules']:
            if_statement = raw_rule['if']
            action_statement = raw_rule['action']
            input_rules.append([if_statement, action_statement])

        return input_rules
