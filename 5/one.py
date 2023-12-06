
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
                tables[table_key].append((int(dest_range_start), int(source_range_start), int(range_size)))

            elif not line:
                table_index += 1
                continue

            elif line[0].isalpha():
                continue

        except IndexError:
            break
        

    

def seed_to_location(seed):
    source_number = int(seed)


    for key, value in tables.items():

        for line in value:
            dest_range_start = line[0]
            source_range_start = line[1]
            range_size = line[2]

            if source_range_start <= source_number < source_range_start + range_size:
                source_number = source_number + (dest_range_start - source_range_start)
                break
            else:
                continue

    return source_number
        
lowest_location = 0


for index, seed in enumerate(seeds):
    seed = int(seed)
    location = seed_to_location(seed)

    if index == 0:
        lowest_location = location
    else:
        if lowest_location > location:
            lowest_location = location

print(lowest_location)