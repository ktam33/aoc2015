import re

def get_distance_at(velocity, fly_time, rest_time, at_time):
    cycle_time = fly_time + rest_time
    cycle_dist = velocity * fly_time
    cycles, remainder = divmod(at_time, cycle_time)
    last_dist = remainder * velocity if remainder < fly_time else cycle_dist

    return cycles * cycle_dist + last_dist

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

answer = 0
for line in lines:
    match = re.match(r'\w+ can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\.', line)
    velocity = int(match.group(1))
    fly_time = int(match.group(2))
    rest_time = int(match.group(3))
    dist = get_distance_at(velocity, fly_time, rest_time, 2503)
    if dist > answer:
        answer = dist
print(answer)
