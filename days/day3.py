from day import Day

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
    

def get_description_and_result() -> tuple[str, str]:
    rucksacks = get_input_lines()
    
    total_priority = 0
    
    for rucksack in rucksacks:
        compartment_size = int(len(rucksack)/2)

        first_compartment = rucksack[:compartment_size]
        second_compartment = rucksack[compartment_size:-1]
        
        print(first_compartment)
        print(second_compartment)
        
    
    pass
    
    description = f""
    result = f"" 
            
    return description, result
    
def main() -> None:
    description, result = get_description_and_result()
    print(description)
    print("---------------------------------------------------------------------------")
    print(result)
    print("---------------------------------------------------------------------------")

def getDay() -> Day:
    description, result = get_description_and_result()
    
    day = Day(DAY_NUMBER)
    day.set_description(description)
    day.set_result(result)
    
    return day

if __name__ == "__main__":
    main()