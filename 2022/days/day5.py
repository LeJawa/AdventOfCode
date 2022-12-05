from argument_parser import get_config_from_individual_day
import os

from day import Day
DAY = 5

def separate_layout_and_instructions(lines: list[str]) -> tuple[list[str], list[str]]:
    cutoff_line_number = -1
    current_line_number = 1
    for line in lines:
        if line == '\n':
            cutoff_line_number = current_line_number
            break
        current_line_number += 1
    
    return lines[:cutoff_line_number-1], lines[cutoff_line_number:]

def parse_raw_layer(raw_layer: str) -> list[str]:
    stack_width = 4
    number_of_stacks = int( len(raw_layer) / stack_width )
    
    layer = []
    for stack in range(number_of_stacks):
        layer.append(raw_layer[1 + stack*stack_width])
    
    return layer 

def parse_initial_raw_layout(initial_raw_layout: list[str]) -> list[list[str]]:
    initial_raw_layout = initial_raw_layout[::-1]
    
    stacks: list[list[str]] = []
    for _ in range(len(parse_raw_layer(initial_raw_layout[0]))):
        stacks.append([])
    
    for raw_layer in initial_raw_layout[1:]:
        layer = parse_raw_layer(raw_layer)
        
        for stack_number in range(len(layer)):
            if layer[stack_number] != ' ':
                stacks[stack_number].append(layer[stack_number])
    return stacks

def parse_single_instruction(instruction_raw: str) -> tuple[int, int, int]:
    instruction_list = instruction_raw.split()
    return int(instruction_list[1]), int(instruction_list[3])-1, int(instruction_list[5])-1
    
def run_day(day: Day) -> Day:
    lines = day.input
    
    initial_raw_layout, instructions_raw = separate_layout_and_instructions(lines)
    
    # stacks is a list of lists. Each list represents the contents of a specific stack.
    stacks1 = parse_initial_raw_layout(initial_raw_layout)
    stacks2 = parse_initial_raw_layout(initial_raw_layout)
    
    for instruction_raw in instructions_raw:
        quantity, source, destination = parse_single_instruction(instruction_raw)
        
        stacks2[destination] += stacks2[source][-quantity:]
        
        for _ in range(quantity):
            stacks1[destination].append(stacks1[source].pop())
            stacks2[source].pop()
            
            
    top_boxes1 = ''
    top_boxes2 = ''
    for stack in stacks1:
        top_boxes1 += stack[-1]
    for stack in stacks2:
        top_boxes2 += stack[-1]  
    
    day.set_description(f"The elves are rearranging {sum([len(stack) for stack in stacks2])} crates.")
    day.set_result(f"With the CrateMover 9000, the top crates after all the instructions would be: {top_boxes1}\n" \
        + f"With the CrateMover 9001, the top crates after all the instructions are actually: {top_boxes2}")
            
    return day


if __name__ == "__main__":
    
    PATH = os.path.dirname(__file__)
    
    config = get_config_from_individual_day()

    PRINT_OUTPUT = not config['no_output']
        
    day = Day(DAY)
    day.set_input(f"{PATH}/../input/")
    day = run_day(day)
    day.append_to_output(PATH)
    
    if PRINT_OUTPUT:
        print(day)