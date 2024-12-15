import json
with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]
input = lines[0]

def traverse(obj):
    total = 0
    if isinstance(obj, dict):
        if "red" not in obj.values():
            for key in obj:
                total += traverse(obj[key])
        else: 
            return 0
    elif isinstance(obj, list):
        for item in obj:
            total += traverse(item)
    elif isinstance(obj, int):
        return obj
    elif isinstance(obj, str):
        return 0
    
    return total

obj = json.loads(input)
print(traverse(obj))