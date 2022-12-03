import os
import re
import sys
sys.path.append("days/")

def createImports() -> None:
    days = re.findall(r'(day\d+)\.py', str(os.listdir("days")))
    
    with open("import_days.py", 'w') as f:
        f.write("# * This file was created automatically *\n\n")
        
        for day in days:
            f.write(f"import {day}\n")
        
        f.write("\ndef get_days():\n    days = []\n    ")
        
        for day in days:
            f.write(f"days.append({day}.get_day())\n    ")
        
        f.write("\n    return days\n")
    
createImports()

from import_days import get_days

days = get_days()

for day in days:
    print(day)

    