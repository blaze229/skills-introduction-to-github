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
            if 'deepLink' in item:
                deep_link = item['deepLink']
                # regex to ensure deepLink matches expected GitHub URL format
                if not re.match(r'^https://github\.com/.*', deep_link):
                    print(f"Invalid deepLink format: {deep_link}")
                    sys.exit(1)
            else:
                pass

    except Exception as e:
        print(f"Error validating report: {e}")
        sys.exit(1)

if __name__ == '__main__':
    validate()
