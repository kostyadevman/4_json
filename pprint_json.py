import json
import sys
import os

def load_data(filepath):
    if os.path.isfile(filepath):
        with open(filepath, 'r') as outfile:
            try:
                raw_json_data = json.loads(outfile.read())
            except ValueError as  e:
                print('Json open failed:')
                print(e)
                return None
        return raw_json_data
    else:
        print("File '{}' doesn't exists".format(filepath))
        return None

def pretty_print_json(data):
    pretty_json_data = json.dumps(data, ensure_ascii=False, indent=4)
    print(pretty_json_data)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python pprint_json.py <path to file>')
    else:
        json_data = load_data(sys.argv[1])
        if data != None:
            pretty_print_json(data)

