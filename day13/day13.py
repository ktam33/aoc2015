import re
import itertools

with open("input.txt", "r") as file:
    lines = [line.strip() for line in file]

people = {}

for line in lines:
    match = re.match(r'(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).', line)
    person_a = match.group(1)
    gain_or_lose = match.group(2)
    units = int(match.group(3)) if gain_or_lose == "gain" else -int(match.group(3))
    person_b = match.group(4)
    if person_a not in people:
        people[person_a] = {}
    people[person_a][person_b] = units

all_combinations = [x for x in itertools.permutations(people)]

highest = 0
for combination in all_combinations:
    cost = 0
    for i in range(len(combination)):
        if i < len(combination) - 1:
            cost += people[combination[i]][combination[i + 1]] + people[combination[i + 1]][combination[i]]
        else:
            cost += people[combination[i]][combination[0]] + people[combination[0]][combination[i]]
    if cost > highest:
        highest = cost
print(highest)


