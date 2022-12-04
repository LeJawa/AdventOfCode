from argument_parser import get_config_from_individual_day
import os

from day import Day
DAY = 1

def run_day(day: Day) -> Day:
    directions = day.input[0]
    
    floor = 0
    steps = 1
    basement_direction = -1
    
    for direction in directions:
        if direction == '(':
            floor += 1
        else:
            floor -= 1
        
        if floor == -1 and basement_direction == -1:
            basement_direction = steps
        
        steps += 1
    
    day.set_description(f"Santa needs to find the correct floor.")
    day.set_result(f"He goes to the {floor}th floor.\nBut not without first visiting the basement with the {basement_direction}th direction.")
            
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