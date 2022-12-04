from argument_parser import get_config_from_individual_day
import os

from day import Day
DAY = 1

def run_day(day: Day) -> Day:
    lines = day.input
    
    caloriesPerElf = []
    elfCalories = 0

    for line in lines:
        line = line.strip()
        if line == '':
            caloriesPerElf.append(elfCalories)
            elfCalories = 0
            continue
    
        elfCalories += int(line)

    # This is really clever.
    # First element is a list from 0 to NumberOfElves, i.e. length of caloriesPerElf.
    # Second element is the key which converts each element of the first list into its corresponding calories.
    # reverse is just to get descending ordering.
    # sorted will then sort the first list as if it contained the calories given by the key.
    # The final list will not contain the calories, but the numbers from 0 to NumberOfElves.
    orderedListOfElves = sorted(list(range(len(caloriesPerElf))), key = lambda i: caloriesPerElf[i], reverse=True)
    orderedListOfCalories = [caloriesPerElf[elf] for elf in orderedListOfElves]
    
    day.set_description(f"In the jungle there are {len(caloriesPerElf)} elves carrying calories.")
    day.set_result(f"Elf #{orderedListOfElves[0]} is carrying the most calories: {orderedListOfCalories[0]}\n\n" \
            + f"The top three elves carrying calories are: elf #{orderedListOfElves[0]}, elf #{orderedListOfElves[1]} and elf #{orderedListOfElves[2]}\n" \
            + f"They are carrying a total of {sum(orderedListOfCalories[:3])} calories")
            
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