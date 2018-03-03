import json
import sys
import os

def load_data(filepath):
    if os.path.isfile(filepath):
        with open(filepath, 'r') as infile:
            json_content = json.loads(infile.read())
        return json_content
    else:
        return None

def pretty_print_json(json_content):
    pretty_json_content = json.dumps(json_content, ensure_ascii=False, indent=4)

    return pretty_json_content

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python pprint_json.py <path to file>')
    else:
        json_content = load_data(sys.argv[1])
        if json_content:
            pretty_json_content = pretty_print_json(json_content)
            print(pretty_json_content)
        else:
            print('File doesn\'t exist')

