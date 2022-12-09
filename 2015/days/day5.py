from argument_parser import get_config_from_individual_day
import os

from day import Day
DAY = 5

def is_nice_part_one(string: str) -> bool:    
    naughty_substring_list = ['ab', 'cd', 'pq', 'xy']
    for substring in naughty_substring_list:
        if substring in string:
            return False
        
    number_of_vowels = 0
    repeated_letter = False
    last_letter = None
    for letter in string:
        if letter in ['a', 'e', 'i', 'o', 'u']:
            number_of_vowels += 1
        
        if last_letter == None:
            last_letter = letter
        else:
            if last_letter == letter:
                repeated_letter = True
            last_letter = letter
        
    if number_of_vowels < 3:
        return False
    
    if not repeated_letter:
        return False
    
    return True   

def is_nice_part_two(string: str) -> bool:
    
    repeatead_letter = False
    repeatead_pair = False  
    
    for i in range(len(string) - 2):
        if string[i] == string[i+2]:
            repeatead_letter = True
            break
        
    
    for i in range(len(string) - 3):
        substring = string[i:i+2]
        if substring in string[i+2:]:
            repeatead_pair = True
            break         
        
    return repeatead_pair and repeatead_letter

def run_day(day: Day) -> Day:
    strings = day.input
    
    nice_strings_part_one = 0
    nice_strings_part_two = 0
    
    for string in strings:
        if is_nice_part_one(string):
            nice_strings_part_one += 1
        if is_nice_part_two(string):
            nice_strings_part_two += 1
    
    day.set_description(f"Santa has two ways of figuring out which strings are nice and which are naughty.")
    day.set_result(f"According to the first way, there are {nice_strings_part_one} nice strings.\nAccording to the second way, there are {nice_strings_part_two} nice strings.")
            
    return day


if __name__ == "__main__":
    
    PATH = os.path.dirname(__file__)
    
    config = get_config_from_individual_day()

    PRINT_OUTPUT = not config['no_output']
        
    day = Day(DAY)
    day.set_input(f"{PATH}/../input/")
    day = run_day(day)
    day.append_to_output(PATH)
    
    if PRINT_OUTPUT:
        print(day)