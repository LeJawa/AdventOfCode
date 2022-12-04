from argument_parser import get_config_from_individual_day
import os

from day import Day
DAY = 5

def is_nice(string: str) -> bool:    
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
        
    if number_of_vowels < 3:
        return False
    
    if not repeated_letter:
        return False
    
    return True   
    

def run_day(day: Day) -> Day:
    strings = day.input
    
    nice_strings = 0
    
    for string in strings:
        if is_nice(string):
            nice_strings += 1
    
    day.set_description(f"")
    day.set_result(f"{nice_strings}")
            
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