import json
import sys
import os


def load_data(filepath):
    if os.path.isfile(filepath):
        with open(filepath, 'r') as infile:
            json_content = json.loads(infile.read())
        return json_content


def make_pretty_json(json_content):
    pretty_json_content = json.dumps(json_content, ensure_ascii=False, indent=4)

    return pretty_json_content


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit('Usage: python pprint_json.py <path to file>')
    json_content = load_data(sys.argv[1])
    if json_content:
        pretty_json_content = make_pretty_json(json_content)
        print(pretty_json_content)

