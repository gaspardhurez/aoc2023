
total = 0

with open('input.txt', 'r') as file:
    lines = file.readlines()

    for line_index, line in enumerate(lines):
        # if line_index != 89: continue

        green = 0
        red = 0
        blue = 0

        id, line = line.split(':', 1)
        id = int(id.strip('Game '))
        line = line.replace(';', ',').replace(' ', '')
        # print(line)
        
        for index, char in enumerate(line):

            try:
                current_draw, line = line.split(",", 1)

                if current_draw[1].isdigit():
                    color = current_draw[2]
                    amount = int(current_draw[0:2])
                else:
                    color = current_draw[1]
                    amount = int(current_draw[0])

            except ValueError:
                if line[1].isdigit():
                    color = line[2]
                    amount = int(line[0:2])
                else:
                    color = line[1]
                    amount = int(line[0])
                
            if color == 'r':
                if amount > red:
                    red = amount
            if color == 'g':
                if amount > green:
                    green = amount
            if color == 'b':
                if amount > blue:
                    blue = amount
            # print(line)
            # print(color)
            # print(amount)
        
        
        line_total = red * green * blue
        total += line_total
        
        print("Line:", line_index)
        print("Red:", red)
        print("Green:", green)
        print("Blue:", blue)
        print(line_total)
        print(total)
        

    print(total)

            
            
