import re

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

ingredients = []
for line in lines:
    reg_ex = r'\w+: capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)'
    match = re.match(reg_ex, line)
    ingredients.append((int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))))


high_score = 0
for a in range(1, 98):
    for b in range (1, 98 - a):
        for c in range (1, 98 - (a + b)):
            d = 100 - (a + b + c)
            cookie = []
            cookie.append(tuple([i * a for i in ingredients[0]]))
            cookie.append(tuple([i * b for i in ingredients[1]]))
            cookie.append(tuple([i * c for i in ingredients[2]]))
            cookie.append(tuple([i * d for i in ingredients[3]]))
            capacity = sum([c[0] for c in cookie])
            if capacity < 0:
                capacity = 0
            durability = sum([c[1] for c in cookie])
            if durability < 0:
                durability = 0
            flavor = sum([c[2] for c in cookie])
            if flavor < 0:
                flavor = 0
            texture = sum([c[3] for c in cookie])
            if texture < 0:
                texture = 0
            score = capacity * durability * flavor * texture
            if score > high_score:
                high_score = score
            
print(high_score)