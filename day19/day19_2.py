import re
import functools
with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

split_index = lines.index('')
goal = lines[split_index + 1]
instructions_strings = lines[:split_index]
instructions = set()
for i_str in instructions_strings:
    match = re.match(r'(\w+) => (\w+)', i_str)
    instructions.add((match.group(1), match.group(2)))

def replace_longest(current):
    longest_instruction = None
    for instruction in instructions:
        if re.search(instruction[1], current):
            if longest_instruction == None:
                longest_instruction = instruction
            elif len(instruction[1]) >= len(longest_instruction[1]):
                if len(current) > 3 and instruction[0] == 'e':
                    pass
                else: 
                    longest_instruction = instruction

    match = re.search(longest_instruction[1], current)
    return current[:match.start()] + instruction[0] + current[match.end():]
    

        

@functools.cache
def get_new_molecules(start):
    new_molecules = set()
    for instruction in instructions:
        for match in re.finditer(instruction[0], start):
            new_molecules.add(start[:match.start()] + instruction[1] + start[match.end():])
    return new_molecules

@functools.cache
def find_molecule(start, goal, depth):
    print(start)
    found_depths = []
    next_molecules = get_new_molecules(start)
    for molecule in next_molecules:
        if molecule == goal:
            found_depths.append(depth + 1)
        elif len(molecule) >= len(goal):
            pass
        else:
            found_depths.extend(find_molecule(molecule, goal, depth + 1))
    return found_depths

current = goal

while current != 'e':
    print(len(current))
    current = replace_longest(current)
    print(current)

