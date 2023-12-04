import re

total = 0

number_mapping = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9,
}

input = input("Index: ")

with open('input.txt', 'r') as file:
    lines = file.readlines()

    for line_index, line in enumerate(lines):
        words = []
        digits = []

        # Identify digits
        for index, char in enumerate(line):
            if char.isdigit():
                digits.append([char, index])

        # Identify word numbers
        for key, value in number_mapping.items():
            specific_line = line
            while key in specific_line:
                specific_line = specific_line.split(key, 1)[1]
                key_index = len (line) - len(specific_line) - len(key) + 1
                words.append([key, key_index])
                

        # Convert words to digits
        for word in words:
            word[0] = str(number_mapping[word[0]])

        numbers = words + digits
        sorted_numbers = sorted(numbers, key=lambda x: x[1])
        
        first_digit = sorted_numbers[0][0]
        last_digit = sorted_numbers[len(sorted_numbers) - 1][0]
        line_total = int(first_digit + last_digit)

        total += line_total

        if str(line_index) == input:
            print(sorted_numbers)
            print(line_total)



print(total)
