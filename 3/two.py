gears = []
numbers = []
total = 0

with open('input.txt', 'r') as file:

    # Extract positions from symbols and numbers for each line
    lines = file.readlines()

    for line_index, line in enumerate(lines):
        line_gears = []
        line_numbers = []

        chars_to_skip = 0

        for index, char in enumerate(line):

            if chars_to_skip > 0:
                chars_to_skip -= 1
                continue

            if char == '*':
                gears.append((line_index, index))
        
            elif char.isdigit():
                number = char
                for next_char in line[index + 1:]:
                    if next_char.isdigit():
                        number += next_char
                    else:
                        break
                  
                line_numbers.append((number, index, len(number)))
                chars_to_skip = len(number) - 1
            
            else:
                continue
                        
        numbers.append(line_numbers)

    
    print (gears[0:30])

    # Check for adjacent numbers

        

    for gear in gears:
        gear_row = gear[0]
        gear_index = gear[1]
        adjacent_numbers = []

        if gear_row == 0:
            numbers_range = numbers[gear_row: gear_row + 2]
        elif gear_row == len(numbers) - 1:
            numbers_range = numbers[gear_row-1: gear_row +1]
        else:
            numbers_range = numbers[gear_row-1: gear_row+2]

        for number_line in numbers_range:
            for number_tuple in number_line:
                number = int(number_tuple[0])
                number_index = int(number_tuple[1])
                number_length = int(number_tuple[2])

                if gear_index == 0:
                    if number_index <= 1:
                        adjacent_numbers.append(number)
                        continue

                else:
                    for i in range(number_index, number_index + number_length):
                        if gear_index - 1 <= i <= gear_index + 1:
                            adjacent_numbers.append(number)
                            break
                    continue
        
        if len(adjacent_numbers) == 2:
            product = adjacent_numbers[0] * adjacent_numbers[1]
            total += product



    
    print(total)
        
