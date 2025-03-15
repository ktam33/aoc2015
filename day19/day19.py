import re
with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

split_index = lines.index('')
original = lines[split_index + 1]
instructions = lines[:split_index]

new = set()

for instruction in instructions:
    i_match = re.match(r'(\w+) => (\w+)', instruction)
    for match in re.finditer(i_match.group(1), original):
        new.add(original[:match.start()] + i_match.group(2) + original[match.end():])

print(new)
print(len(new))