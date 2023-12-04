symbols = []
numbers = []
total = 0

test = int(input("Test: ")) - 1


with open('input.txt', 'r') as file:

    # Extract positions from symbols and numbers for each line
    lines = file.readlines()

    for line_index, line in enumerate(lines):
        line_symbols = []
        line_numbers = []

        chars_to_skip = 0

        for index, char in enumerate(line):

            if chars_to_skip > 0:
                chars_to_skip -= 1
                continue

            if char == '.' or char =='\n':
                continue
                
            elif not char.isdigit():
                line_symbols.append(index)

        
            elif char.isdigit():
                number = char
                for next_char in line[index + 1:]:
                    if next_char.isdigit():
                        number += next_char
                    else:
                        break
                  
                line_numbers.append((number, index, len(number)))
                chars_to_skip = len(number) - 1
                        
        symbols.append(line_symbols)
        numbers.append(line_numbers)
    
    print(symbols[test])
    print(numbers[test])


    for line_index, line in enumerate(numbers):
        for number_tuple in line:
            number = int(number_tuple[0])
            number_index = int(number_tuple[1])
            number_length = int(number_tuple[2])


        # Check for adjacent numbers
    for line_index, line in enumerate(numbers):

        if line_index == 0:
            symbols_range = symbols[line_index: line_index+2]
        elif line_index == len(numbers) - 1:
            symbols_range = symbols[line_index-1: line_index+1]
        else:
            symbols_range = symbols[line_index-1: line_index+2]
        
        adjacent_numbers = []

        for number_tuple in line:
            number = int(number_tuple[0])
            number_index = int(number_tuple[1])
            number_length = int(number_tuple[2])
            adjacent = False

            for symbol_line in symbols_range:
                if adjacent:
                    break
                for symbol_index in symbol_line:
                    symbol_index = int(symbol_index)

                    if number_index == 0:
                        if number_index <= symbol_index <= number_index + number_length:
                            total += number
                            adjacent_numbers.append(number)
                            adjacent = True
                            break

                    else:
                        if number_index - 1 <= symbol_index <= number_index + number_length:
                            total += number
                            adjacent = True
                            adjacent_numbers.append(number)
                            if number == 929:
                                print(symbol_index)
                            break

        if line_index == test:
            print(adjacent_numbers)
        
        
    
    
    print(total)
        
