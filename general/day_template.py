from argument_parser import get_config
import os

from day import Day
DAY = 0

def run_day(day: Day) -> Day:
    lines = day.input
    
     # Calculate output
    
    day.set_description(f"")
    day.set_result(f"")
            
    return day


if __name__ == "__main__":
    
    PATH = os.path.dirname(__file__)
    
    config = get_config()

    PRINT_OUTPUT = not config['no_output']
        
    day = Day(DAY)
    day.set_input(f"{PATH}/../input/")
    day = run_day(day)
    day.append_to_output(PATH)
    
    if PRINT_OUTPUT:
        print(day)