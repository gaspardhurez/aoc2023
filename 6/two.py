with open('input.txt', 'r') as file:
    lines = file.readlines()

    index = 0
    time = int(lines[0].split(':')[1].strip().replace(' ', ''))
    distance = int(lines[1].split(':')[1].strip().replace(' ', ''))

print(time, distance)

winning_scenarios = 0


scenarios = range(time + 1)

for scenario in scenarios:
    speed = scenario
    seconds_to_race = time - scenario
    travel_distance = speed * seconds_to_race

    if travel_distance > distance:
        winning_scenarios += 1
    

print(winning_scenarios)
