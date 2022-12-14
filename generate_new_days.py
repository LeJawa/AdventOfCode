from argument_parser import get_config_for_new_days_generation
import os
import re
import shutil
from pathlib import Path

YEAR = 2022

def parse_year_input(year_input: str) -> int:
    if year_input is None:
        return YEAR
    
    return int(year_input)
    
def parse_day_input(days_input: str) -> list[int]:
    days: list[int] = []
    
    if days_input is None:
        return days
    
    tmp = days_input.split(sep=',')
    
    for day in tmp:
        if '-' in day:
            tmp2 = day.split(sep='-')
            for d in [i for i in range(int(tmp2[0]),int(tmp2[1])+1)]:
                days.append(d)
        else:
            days.append(int(day))
    
    # Removes duplicates
    days = list(dict.fromkeys(days))

    days.sort()
    
    return days

def create_year_folder_hierarchy(year: int) -> None:
    try:
        os.makedirs(f"{year}/days/")
        os.makedirs(f"{year}/input/")
        os.makedirs(f"{year}/output/")
    except FileExistsError as error:
        print("Folders already exist")

def create_input_day_file(path: str, day: int) -> None:
    Path(os.path.join(path, f"day{day}.txt")).touch()

def create_python_day_file(path: str, day: int) -> None:
    shutil.copyfile(os.path.join("general", f"day_template.py"), os.path.join(path, f"day{day}.py"))

def create_files(year: int, days: list[int]) -> None:
    create_year_folder_hierarchy(year)
    
    days_path = os.path.join(str(year), "days")
    input_path = os.path.join(str(year), "input")
    
    days_present = re.findall(r'day(\d+)\.py', str(os.listdir(days_path)))
    days_present = [int(day) for day in days_present]
    days_present.sort()

    last_day = 0
    if days_present != []:
        last_day = days_present[-1]
        
    if days == []:
        if last_day < 25:
            create_python_day_file(days_path, last_day + 1)
            create_input_day_file(input_path, last_day + 1)
        else:
            print(f"There are already 25 days created in the year {year}.")
        return
    
    for day in days:
        if day > 25:
            print("Day higher than 25 found. Stopping.")
            return
        
        if day not in days_present:
            create_python_day_file(days_path, day)
            create_input_day_file(input_path, day)
        else:
            print(f"Skipping day {day} because already present.")


config = get_config_for_new_days_generation()

year = parse_year_input(config['year'])
days = parse_day_input(config['days'])

create_files(year, days)


