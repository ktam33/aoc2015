import re

def get_distance_at(velocity, fly_time, rest_time, at_time):
    cycle_time = fly_time + rest_time
    cycle_dist = velocity * fly_time
    cycles, remainder = divmod(at_time, cycle_time)
    last_dist = remainder * velocity if remainder < fly_time else cycle_dist

    return cycles * cycle_dist + last_dist

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

reindeers = {}
answer = 0

for line in lines:
    match = re.match(r'\w+ can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\.', line)
    velocity = int(match.group(1))
    fly_time = int(match.group(2))
    rest_time = int(match.group(3))
    reindeers[(velocity, fly_time, rest_time)] = [0, 0]

race_time = 2503
for i in range(1, race_time + 1):
    for reindeer in reindeers:
        reindeers[reindeer][0] = get_distance_at(reindeer[0], reindeer[1], reindeer[2], i)

    max_dist = max([reindeers[r][0] for r in reindeers])
    winners = [r for r in reindeers if reindeers[r][0] == max_dist]
    for winner in winners:
        reindeers[winner][1] += 1

print(max([reindeers[r][1] for r in reindeers]))


