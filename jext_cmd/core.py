import json
import sys

def extract(raw_json, target_field):
    return json.loads(raw_json)[target_field]

def main():
    field = sys.argv[1]
    user_input_stdin = sys.stdin.read()
    sys.stdout.write(json.dumps(extract(user_input_stdin, field))+'\n')