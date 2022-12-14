from argument_parser import get_config_from_individual_day
import os
import re

from day import Day
DAY = 11
PRINT_OUTPUT_MANUAL_OVERRIDE = True

class Monkey:
    def __init__(self, description: list[str], worry_diminishes: bool) -> None:
        self.parse_description(description)
        
        self.worry_diminishes = worry_diminishes
        self.activity = 0
        
        self.monkey_modulus = 1
        
    def parse_description(self, description: list[str]) -> None:
        self.number = int(re.findall('\d+', description[0])[0])
        
        self.items = [int(x) for x in description[1].replace(',', ' ').split()[2:]]
        
        self.parse_operation(description[2])
        
        self.divisor_test = int(description[3].split()[-1])
        
        self.monkey_if_true = int(description[4].split()[-1])
        self.monkey_if_false = int(description[5].split()[-1])
        
    def parse_operation(self, operation_raw:str) -> None:
        right = operation_raw.split()[-1]
        
        self.right_is_old = False
        if right == 'old':
            self.right_is_old = True
        else:
            self.right = int(right)
            
        self.operation = operation_raw.split()[-2]
        
    def do_operation(self, old: int) -> int:
        if self.right_is_old:
            self.right = old
        if self.operation == '+':
            return old + self.right
        else:
            return old * self.right
        
    def inspect_next_item(self) -> tuple[int, int]: # Monkey index, item worry level
        if len(self.items) == 0:
            return None, None
        
        self.activity += 1
        
        worry_level = self.items[0]
        worry_level = self.do_operation(worry_level)
        
        if self.worry_diminishes:
            worry_level //= 3
        
        self.items = self.items[1:]
        
        if worry_level % self.divisor_test == 0:
            return self.monkey_if_true, worry_level
        else:
            return self.monkey_if_false, worry_level
        
    def add_item(self, worry_level: int) -> None:
        self.items.append(worry_level % self.monkey_modulus)
        
    def has_items(self) -> bool:
        return len(self.items) > 0

def simulate_monkey_business(monkey_description: list[str], rounds: int, worry_diminishes: bool) -> list[int]:
    monkey_start = 0
    monkey_end = 6
    MONKEY_DESCRIPTION_LENGTH = 7
    
    monkeys: list[Monkey] = []
    
    # The modulus keeps all worry numbers from spiralling out of control
    # Each number is set to the result of number % monkey_modulus
    # The idea is that any number higher than monkey_modulus will behave exactly like number % monkey_modulus
    monkey_modulus = 1
    
    while(monkey_start<len(monkey_description)):
        monkeys.append(Monkey(monkey_description[monkey_start:monkey_end], worry_diminishes))
        monkey_start += MONKEY_DESCRIPTION_LENGTH
        monkey_end += MONKEY_DESCRIPTION_LENGTH
        
        monkey_modulus *= monkeys[-1].divisor_test
    
    for monkey in monkeys:
        monkey.monkey_modulus = monkey_modulus
    
        
    for round in range(rounds):
        for monkey in monkeys:
            while monkey.has_items():
                monkey_to_throw, item = monkey.inspect_next_item()
                monkeys[monkey_to_throw].add_item(item)
    
    activity = []    
    for monkey in monkeys:
        activity.append(monkey.activity)
    
    activity.sort(reverse=True)
    
    return activity[0]*activity[1]



def run_day(day: Day) -> Day:
    lines = day.input
    # lines = day.sample
    
    monkey_business_1 = simulate_monkey_business(lines, 20, True)
    monkey_business_2 = simulate_monkey_business(lines, 10000, False)
        
    
    day.set_description(f"Some monkeys have stolen my items and are exchanging them by throwing them at each other.")
    day.set_result(f"While my worry levels were still reducing, the total monkey business was {monkey_business_1}.\n" + \
        f"Now that I can no longer keep calm, the monkey business is {monkey_business_2}.")
            
    return day


if __name__ == "__main__":
    
    PATH = os.path.dirname(__file__)
    
    config = get_config_from_individual_day()

    PRINT_OUTPUT = not config['no_output']
        
    day = Day(DAY)
    day.set_input(f"{PATH}/../input/")
    day = run_day(day)
    day.append_to_output(PATH)
    
    if PRINT_OUTPUT and PRINT_OUTPUT_MANUAL_OVERRIDE:
        print(day)