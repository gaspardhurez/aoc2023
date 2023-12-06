import numpy as np

tables = {}

# Extract list of seeds
with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

    seeds = lines[0].split(':', 1)[1].strip().split()
    lines = lines[2:]

    for line_index, line in enumerate(lines):
        if line and line[0].isalpha():
            table_name = line.split(' ', 1)[0]
            tables[table_name] = []

    
    table_index = 0
    for line_index, line in enumerate(lines):

        try:
            if line and line[0].isdigit():

                dest_range_start, source_range_start, range_size = line.split(' ', 2)
                table_key = list(tables.keys())[table_index]
                tables[table_key].append(np.array([int(dest_range_start), int(source_range_start), int(range_size)]))

            elif not line:
                table_index += 1
                continue

            elif line[0].isalpha():
                continue

        except IndexError:
            break

    for key, value in tables.items():
        tables[key] =  np.array(tables[key])
        

def seed_to_location(seed):
    source_number = int(seed)

    for key, value in tables.items():

        mask = (value[:, 1] <= source_number) & (source_number < value[:, 1] + value[:, 2])
        if value[mask].any():
            dest_range_start, source_range_start, range_size = value[mask][0]
            source_number = source_number + (dest_range_start - source_range_start)
        else:
            continue
        

    return source_number


seeds_range = []
seeds_values = []

for index, seed in enumerate(seeds):

    if index % 2 == 0:
        seeds_values.append(int(seeds[index]))
    else:
        seeds_range.append(int(seeds[index]))

for seed_index, seed in enumerate(seeds_values):
    print(seed_index)
    lowest_location = float('inf')
    current_seed = seed

    while current_seed < seed + seeds_range[seed_index]:
        current_location = seed_to_location(current_seed)
        
        if current_location < lowest_location:
            lowest_location = current_location
        
        current_seed += 1
    

print(lowest_location)
