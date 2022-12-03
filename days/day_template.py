from day import Day

DAY_NUMBER = 0

def get_input_lines() -> list[str]:
    with open(f"inputs/day{DAY_NUMBER}.txt", 'r') as f:
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
    
    day = Day(DAY_NUMBER)
    day.set_description(description)
    day.set_result(result)
    
    return day

if __name__ == "__main__":
    print(get_day())