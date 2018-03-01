import json
import sys
import os

def load_data(filepath):
    if os.path.isfile(filepath):
        with open(filepath, 'r') as f:
            try:
                raw_json_data = json.loads(f.read())
            except ValueError as  e:
                print('Json open failed:')
                print(e)
                exit(2)
        return raw_json_data
    else:
        print("File '{}' doesn't exists".format(filepath))
        exit(1)

def pretty_print_json(data):
    pretty_json_data = json.dumps(data, ensure_ascii=False, indent=4)
    print(pretty_json_data)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python pprint_json.py <path to file>')
    else:
        data = load_data(sys.argv[1])
        pretty_print_json(data)

