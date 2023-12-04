import re
total = 0

with open('input.txt', 'r') as file:
    lines = file.readlines()
    
    for line_index, line in enumerate(lines):
        # if not line_index == 1:
                # continue
                

        winning_numbers = []
        matches = []
        card_points = 0

        winning_set, draw_set = line.split('|')
        number, winning_set = winning_set.split(':')
        draw_set = draw_set[1:-1]
        winning_set = winning_set[1:-1]

        

        for char in winning_set:
            if winning_set[0] == ' ':
                    winning_set = winning_set[1: ]
            try:
                number, winning_set = winning_set.split(' ', 1)
                winning_numbers.append(number)
                if winning_set[0] == ' ':
                    winning_set = winning_set[1: ]

            except ValueError:
                number = winning_set
                winning_numbers.append(number)
                if winning_set[0] == ' ':
                    winning_set = winning_set[1: ]
                break
                 

        for char in draw_set:
            if draw_set[0] == ' ':
                    draw_set = draw_set[1: ]
            try:
                number, draw_set = draw_set.split(' ', 1)
                if number in winning_numbers:
                    matches.append(number)
                if draw_set[0] == ' ':
                    draw_set = draw_set[1: ]
                
            except ValueError:
                number = draw_set
                if number in winning_numbers:
                    matches.append(number)
                if draw_set[0] == ' ':
                    draw_set = draw_set[1: ]
                break

            

        for index, match in enumerate(matches):
            if index == 0:
                card_points += 1
            else:
                card_points *= 2
            
        total += card_points

        

print(total)


        




        

