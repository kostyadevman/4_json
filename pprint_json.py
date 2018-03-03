import json
import sys
import os

def load_data(filepath):
    if os.path.isfile(filepath):
        with open(filepath, 'r') as infile:
            json_data = json.loads(infile.read())
        return json_data
    else:
        return None

def pretty_print_json(json_data):
    pretty_json_data = json.dumps(json_data, ensure_ascii=False, indent=4)

    return pretty_print_json()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python pprint_json.py <path to file>')
    else:
        json_data = load_data(sys.argv[1])
        if json_data:
            pretty_json_data = pretty_print_json(json_data)
            print(pretty_json_data)
        else:
            print('File doesn\'t exist')

