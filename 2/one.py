
total = 0

with open('input.txt', 'r') as file:
    lines = file.readlines()

    for line_index, line in enumerate(lines):
        green = False
        red = False
        blue = False

        id, line = line.split(':', 1)
        id = int(id.strip('Game '))
        line = line.replace(';', ',').replace(' ', '')
        
        for index, char in enumerate(line):

            try:
                current_draw, line = line.split(",", 1)

                if current_draw[0].isdigit() and current_draw[1].isdigit():
                    
                    if current_draw[2] == 'r':
                        if int(current_draw[0:2])  > 12:
                            red = True
                    elif current_draw[2] == 'g':
                        if int(current_draw[0:2]) > 13:
                            green = True
                    elif current_draw[2] == 'b':
                        if int(current_draw[0:2]) > 14:
                            blue = True
            
            except ValueError:
                if line[0].isdigit() and line[1].isdigit():
                        if line[2] == 'r':
                            if int(line[0:2])  > 12:
                                red = True
                        elif line[2] == 'g':
                            if int(line[0:2]) > 13:
                                green = True
                        elif line[2] == 'b':
                            if int(line[0:2]) > 14:
                                blue = True
        
        if green or red or blue:
            continue
        else:
            total += id
            
    print(total)

            
            
