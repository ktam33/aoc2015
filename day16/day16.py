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

for line in lines:
    match = re.match(r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)', line)
    if (
        the_sue[match.group(2)] == int(match.group(3)) and 
        the_sue[match.group(4)] == int(match.group(5)) and 
        the_sue[match.group(6)] == int(match.group(7))
    ):
        print(f'Sue {match.group(1)}')
    