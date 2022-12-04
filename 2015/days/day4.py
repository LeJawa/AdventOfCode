from argument_parser import get_config_from_individual_day
import os
import hashlib

from day import Day
DAY = 4

def run_day(day: Day) -> Day:
    prefix = day.input[0]
    
    found_one_zero = False
    found_two_zeroes = False
    found_three_zeroes = False
    found_four_zeroes = False
    found_five_zeroes = False
    found_six_zeroes = False
    
    number = 1
    while(not (found_one_zero and found_two_zeroes and found_three_zeroes and found_four_zeroes and found_five_zeroes and found_six_zeroes)):
        hashed_value = hashlib.md5(f"{prefix}{number}".encode('utf-8')).hexdigest()
        
        if hashed_value.startswith('0') and not found_one_zero:
            one_zero_number = number
            found_one_zero = True
        
        if hashed_value.startswith('00') and not found_two_zeroes:
            two_zeroes_number = number
            found_two_zeroes = True
        
        if hashed_value.startswith('000') and not found_three_zeroes:
            three_zeroes_number = number
            found_three_zeroes = True
        
        if hashed_value.startswith('0000') and not found_four_zeroes:
            four_zeroes_number = number
            found_four_zeroes = True
        
        if hashed_value.startswith('00000') and not found_five_zeroes:
            five_zeroes_number = number
            found_five_zeroes = True
        
        if hashed_value.startswith('000000'):
            six_zeroes_number = number
            found_six_zeroes = True
        
        number += 1
            
        
        
    
    day.set_description(f"The elves are mining for AdventCoins and need to find the lowest number which, combined with the key, yields a hash digest with leading zeroes.")
    day.set_result(f"The lowest number found with one leading zero is {one_zero_number}\n" \
        + f"The lowest number found with two leading zeroes is {two_zeroes_number}\n" \
            + f"The lowest number found with three leading zeroes is {three_zeroes_number}\n" \
                + f"The lowest number found with four leading zeroes is {four_zeroes_number}\n" \
                    + f"The lowest number found with five leading zeroes is {five_zeroes_number}\n" \
                        + f"The lowest number found with six leading zeroes is {six_zeroes_number}")
            
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