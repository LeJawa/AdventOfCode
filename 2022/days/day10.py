from argument_parser import get_config_from_individual_day
import os

from day import Day, LITERAL_TEXT_MARKER
DAY = 10
PRINT_OUTPUT_MANUAL_OVERRIDE = True

def get_pixel(cycle, X):
    if cycle == X or cycle == X-1 or cycle == X+1:
        return '#'
    else:
        return ' '

def print_screen(screen):
    s = get_screen_as_str(screen)
    print(s)

def get_screen_as_str(screen):
    s = ''
    for row in screen:
        for pixel in row:
            s += pixel
        s += '\n'
    return s

def run_day(day: Day) -> Day:
    lines = day.input
    # lines = day.sample
    
    iter = lines.__iter__()
    
    X = 1
    adding = False
    cycle = 1
    signal_strengths = []
    
    screen = []
    current_row = -1
    first_row = True
    
    while True:
        if not adding:
            try:
                instruction = iter.__next__().split()
            except StopIteration:
                break
        
        if cycle in [20, 60, 100, 140, 180, 220]:
            signal_strengths.append(cycle * X)
            
        current_column = cycle%40 - 1
        
        if current_column == 0:
            screen.append([])
            current_row += 1
        
        screen[current_row].append(get_pixel(current_column, X))
        
        if len(instruction) == 1: # instruction == ['noop']
            pass
        else:
            if not adding:
                adding = True
            else:
                X += int(instruction[1])
                adding = False
        
        cycle += 1    
    
    day.set_description(f"I need to repair the device video system and figure out what it sends to the screen.")
    day.set_result(f"The sum of the signal strengths is {sum(signal_strengths)}.\n" + \
        f"The screen shows:\n\n{LITERAL_TEXT_MARKER + get_screen_as_str(screen)}")
            
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