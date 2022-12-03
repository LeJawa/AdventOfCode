from day import Day

import re

DAY_NUMBER = 3

def get_input_lines() -> list[str]:
    with open(f"inputs/day{DAY_NUMBER}.txt", 'r') as f:
        lines = f.readlines()
    
    return lines

def get_item_priority(item: str) -> int:
    is_lower = item == item.lower()
    
    if is_lower:
        return ord(item) - 96
    else:
        return ord(item) - 65 + 27

def get_duplicate_item(first_compartment: str, second_compartment: str) -> str:
    for item in first_compartment:
        if item in second_compartment:
            return item
    print(f"No duplicate item found in this rucksack: {first_compartment} : {second_compartment}")

def get_badge_priority(rucksacks_group: list[str]) -> int:
    for item in rucksacks_group[0]:
        if item in rucksacks_group[1] and item in rucksacks_group[2]:
            badge = item
            break

    return get_item_priority(badge)
    

def get_description_and_result() -> tuple[str, str]:
    rucksacks = get_input_lines()
    
    duplicate_priority = 0
    badge_priority = 0
    
    rucksacks_group:list[str] = []
    
    for rucksack in rucksacks:        
        compartment_size = int(len(rucksack)/2)

        first_compartment = rucksack[:compartment_size]
        second_compartment = rucksack[compartment_size:-1]
        
        duplicate_item = get_duplicate_item(first_compartment, second_compartment)
        duplicate_priority += get_item_priority(duplicate_item)
        
        rucksacks_group.append(rucksack)
        
        if len(rucksacks_group) == 3:
            badge_priority += get_badge_priority(rucksacks_group)
            rucksacks_group = []
    
    
    description = f"We need to look for duplicate items in the compartments of {len(rucksacks)} rucksacks as well as finding the badges for each three-Elf group."
    result = f"The total priority of duplicate items between compartments is {duplicate_priority}.\n" \
        + f"The total priority of badges is {badge_priority}." 
            
    return description, result

def get_day() -> Day:
    description, result = get_description_and_result()
    
    day = Day(DAY_NUMBER)
    day.set_description(description)
    day.set_result(result)
    
    return day

if __name__ == "__main__":
    print(get_day())