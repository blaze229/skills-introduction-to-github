import json
import sys
import re

def validate():
    try:
        with open('todo_report.json', 'r') as f:
            data = json.load(f)

        if isinstance(data, list):
            items = data
        elif isinstance(data, dict):
            items = [data]
        else:
            print("Invalid JSON format. Expected list or dict.")
            sys.exit(1)

        for item in items:
            if 'deepLink' not in item:
                print("Missing deepLink in item")
                sys.exit(1)

            deep_link = item['deepLink']

            if not isinstance(deep_link, str):
                print(f"Invalid deepLink type: {type(deep_link)}. Expected string.")
                sys.exit(1)

            # strict regex to ensure deepLink matches expected GitHub URL format for issues/pulls
            if not re.match(r'^https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/(issues|pull)/[0-9]+$', deep_link):
                print(f"Invalid deepLink format: {deep_link}")
                sys.exit(1)

    except Exception as e:
        print(f"Error validating report: {e}")
        sys.exit(1)

if __name__ == '__main__':
    validate()
