from day import Day

DAY_NUMBER = 0

def get_description_and_result() -> tuple[str, str]:
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