import re

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

the_sue = {
'children': 3,
'cats': 7,
'samoyeds': 2,
'pomeranians': 3,
'akitas': 0,
'vizslas': 0,
'goldfish': 5,
'trees': 3,
'cars': 2,
'perfumes': 1,
}

def check_constraint(name, value):
    if name == 'pomeranian' or name == 'goldfish':
        return value < the_sue[name] 
    elif name == 'trees' or name == 'cats':
        return value > the_sue[name]
    else:
        return the_sue[name] == value

for line in lines:
    match = re.match(r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)', line)
    if (
        check_constraint(match.group(2), int(match.group(3))) and 
        check_constraint(match.group(4), int(match.group(5))) and 
        check_constraint(match.group(6), int(match.group(7)))
    ):
        print(f'Sue {match.group(1)}')
    