import argparse
import sys
import os
sys.path.append("general/")

PATH = os.path.dirname(__file__)

from day import Day
DAY = 0

def get_input_lines() -> list[str]:
    with open(f"{PATH}/../input/day{DAY}.txt", 'r') as f:
        lines = f.readlines()
    
    return lines

def get_description_and_result() -> tuple[str, str]:
    lines = get_input_lines()
    
    pass
    
    description = f""
    result = f"" 
            
    return description, result

def get_day() -> Day:
    description, result = get_description_and_result()
    
    day = Day(DAY)
    day.set_description(description)
    day.set_result(result)
    
    return day

parser = argparse.ArgumentParser(description="Day 1 script",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-n", "--no-output", action="store_true", help="Don't show output")
args = parser.parse_args()
config = vars(args)

PRINT_OUTPUT = not config['no_output']

if __name__ == "__main__":
    day = get_day()
    if PRINT_OUTPUT:
        print(day)
    
    day.append_to_output(PATH)