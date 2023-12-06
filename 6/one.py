with open('input.txt', 'r') as file:
    lines = file.readlines()

    index = 0
    time = lines[0].split(':')[1].strip()
    distance = lines[1].split(':')[1].strip()

    race_times = time.split()
    race_times = [int(i) for i in race_times]
    race_distances = distance.split()
    race_distances = [int(i) for i in race_distances]

winning_product = 1

for index, race_time in enumerate(race_times):
    winning_scenarios = 0
    distance_to_beat = race_distances[index]
    scenarios = range(race_time + 1)

    for scenario in scenarios:
        speed = scenario
        seconds_to_race = race_time - scenario
        travel_distance = speed * seconds_to_race

        if travel_distance > distance_to_beat:
            winning_scenarios += 1
    
    winning_product *= winning_scenarios

print(winning_product)

