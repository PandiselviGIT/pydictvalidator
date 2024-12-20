
# Online Python - IDE, Editor, Compiler, Interpreter

import json

def validate_json(data):
    try:
        json.loads(data)
        return True
    except json.JSONDecodeError:
        return False
