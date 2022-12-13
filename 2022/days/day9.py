from argument_parser import get_config_from_individual_day
import os

from day import Day
DAY = 9
PRINT_OUTPUT_MANUAL_OVERRIDE = True

def get_tail_position(head_pos: tuple[int, int], tail_pos: tuple[int, int]) -> tuple[int, int]:
    horizontal_diff = head_pos[0] - tail_pos[0]
    vertical_diff = head_pos[1] - tail_pos[1]
    
    if horizontal_diff in [-1, 0, 1] and vertical_diff in [-1, 0, 1]:
        return tail_pos
    
    horizontal_diff = -1 if horizontal_diff < 0 else 1 if horizontal_diff > 0 else 0
    vertical_diff = -1 if vertical_diff < 0 else 1 if vertical_diff > 0 else 0
    
    return (tail_pos[0] + horizontal_diff, tail_pos[1] + vertical_diff)

def update_position(position: tuple[int, int], delta: tuple[int, int]) -> tuple[int, int]:
    return ( position[0] + delta[0], position[1] + delta[1] )

def run_day(day: Day) -> Day:
    lines = day.input
    
    short_rope = [(0, 0) for _ in range(2)]
    long_rope = [(0, 0) for _ in range(10)]
    
    visited_positions_short = [short_rope[-1]]
    visited_positions_long = [long_rope[-1]]
    
    for line in lines:
        instruction = line.split()
        move = instruction[0]
        qty = int(instruction[1])
        
        if move == 'R':
            delta = (1, 0)
        elif move == 'L':
            delta = (-1, 0)
        elif move == 'U':
            delta = (0, 1)
        else: # move == 'D'
            delta = (0, -1)
        
        short_rope, visited_positions_short = move_head(short_rope, visited_positions_short, delta, qty)
        long_rope, visited_positions_long = move_head(long_rope, visited_positions_long, delta, qty)
    
    day.set_description(f"To pass off time and my own fears, I need to simulate the movement of two different sized ropes after {len(lines)} movement instructions.")
    day.set_result(f"The tail of the short rope visits {len(visited_positions_short)} different positions.\n" + \
        f"The tail of the long rope visits {len(visited_positions_long)} different positions.")
            
    return day

def move_head(rope, visited_positions, delta, qty):
    for _ in range(qty):
        rope[0] = update_position(rope[0], delta)
        for i in range(len(rope)-1):
            rope[i+1] = get_tail_position(rope[i], rope[i+1])
        if rope[-1] not in visited_positions:
            visited_positions.append(rope[-1])
    
    return rope, visited_positions


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