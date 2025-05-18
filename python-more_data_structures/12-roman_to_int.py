#!/usr/bin/python3
def roman_to_int(roman_string):

    try:
        roman_string = roman_string.upper()
    except AttributeError:
        return 0
    if not roman_string:
        return 0

    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    numbers = [roman_dict[char] for char in roman_string]

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            numbers[i - 1] = -numbers[i - 1]

    return sum(numbers)
