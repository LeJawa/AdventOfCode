import os
import re
import sys
sys.path.append("general/")

from day import Day, create_days_from_json

class AdventCalendar:
    def __init__(self, year: int|str) -> None:
        self.year = int(year)
        self.days = []
        
        self.PATH = f"{os.path.dirname(__file__)}/../{year}"
    
    def run_days(self) -> None:
        days_path = f"{self.PATH}/days/"
        day_files:list[str] = re.findall(r'day\d+\.py', str(os.listdir(days_path)))

        for day_file in day_files:
            os.system(f"python {days_path}{day_file} -n")
        
    def import_days(self):
        try:
            self.days = create_days_from_json(f"{self.PATH}/output/out.json")
        except Exception:
            self.run_days()
            self.days = create_days_from_json(f"{self.PATH}/output/out.json")
    
    def print_days(self):
        for day in self.days:
            print(day)
    
    