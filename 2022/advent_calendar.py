import os
import re
import sys
sys.path.append("general/")

from day import Day, create_days_from_json

YEAR = 2022
PATH = os.path.dirname(__file__)

days_path = f"{PATH}/days/"

day_files:list[str] = re.findall(r'day\d+\.py', str(os.listdir(days_path)))

for day_file in day_files:
    os.system(f"python {days_path}{day_file} -n")

days = create_days_from_json(f"{PATH}/output/out.json")

for day in days:
    print(day)

    