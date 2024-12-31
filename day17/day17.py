
containers = []

with open('input.txt', 'r') as file:
    for index, line in enumerate(file):
        containers.append((index, int(line.strip())))

found_combos = set()
goal = 150 if file.name == 'input.txt' else 25

def find_combos(combo):
    total = sum(c[1] for c in combo)
    combos = set()
    for c in containers:
        if c not in combo:
            new_total = c[1] + total
            if new_total <= goal:
                new_combo = combo + (c,)
                new_combo = tuple(sorted(new_combo))
                if new_total == goal:
                    combos.add(new_combo)
                elif combo not in found_combos:
                    combos.update(find_combos(new_combo))
                    found_combos.add(new_combo)
            else:
                pass
    return combos

all_combos = set()
for c in containers:
    all_combos.update(find_combos((c,)))

print(len(all_combos))