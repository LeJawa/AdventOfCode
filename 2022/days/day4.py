from argument_parser import get_config
import os

from day import Day
DAY = 4

def are_fully_contained(bounds1: list[int], bounds2: list[int]) -> bool:
    if bounds1[0] <= bounds2[0] and bounds1[1] >= bounds2[1]:
        return True
    if bounds2[0] <= bounds1[0] and bounds2[1] >= bounds1[1]:
        return True
    return False

def are_overlapping(bounds1: list[int], bounds2: list[int]) -> bool:
    if bounds1[1] < bounds2[0] or bounds2[1] < bounds1[0]:
        return False
    return True

def run_day(day: Day) -> Day:
    pairs = day.input
    
    fully_contained_pairs = 0
    overlapping_pairs = 0
    
    for pair in pairs:
        assigments = pair.strip().split(sep=",")
    
        bounds1 = [int(i) for i in assigments[0].split(sep='-')]
        bounds2 = [int(i) for i in assigments[1].split(sep='-')]
        
        if are_fully_contained(bounds1, bounds2):
            fully_contained_pairs += 1
            
        if are_overlapping(bounds1, bounds2):
            overlapping_pairs += 1
    
    day.set_description(f"The elves have {2*len(pairs)} cleaning assignments. But there are some overlaps...")
    day.set_result(f"There are {fully_contained_pairs} fully contained assignment pairs.\nThere are {overlapping_pairs} overlapping assignment pairs.")
            
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