from argument_parser import get_config_from_individual_day
import os

from day import Day
DAY = 3

def run_day(day: Day) -> Day:
    directions = day.input[0]
    
    santa1_x = 0
    santa1_y = 0
    
    santa2_x = 0
    santa2_y = 0
    
    robot_x = 0
    robot_y = 0
    
    visited_houses_year1 = [(santa1_x,santa1_y)]
    visited_houses_year2 = [(santa2_x,santa2_y)]
    
    number_of_directions = 1
    
    for direction in directions:
        robot_turn = False
        if number_of_directions%2 == 0:
            robot_turn = True
        
        
        if direction == '>':
            santa1_x += 1
            if robot_turn:
                robot_x += 1
            else:
                santa2_x += 1
        elif direction == '<':
            santa1_x -= 1
            if robot_turn:
                robot_x -= 1
            else:
                santa2_x -= 1
        elif direction == '^':
            santa1_y += 1
            if robot_turn:
                robot_y += 1
            else:
                santa2_y += 1
        elif direction == 'v':
            santa1_y -= 1
            if robot_turn:
                robot_y -= 1
            else:
                santa2_y -= 1
        
        if (santa1_x, santa1_y) not in visited_houses_year1:
            visited_houses_year1.append((santa1_x, santa1_y))
            
        
        if (santa2_x, santa2_y) not in visited_houses_year2:
            visited_houses_year2.append((santa2_x, santa2_y))
        if (robot_x, robot_y) not in visited_houses_year2:
            visited_houses_year2.append((robot_x, robot_y))
    
        number_of_directions += 1
    
    
    day.set_description(f"An elf is feeding {len(directions)} directions to Santa the first year, and to Santa and Robo-Santa the next year.")
    day.set_result(f"The first year, Santa visited {len(visited_houses_year1)} houses.\nThe second year, Santa and Robo-Santa visited {len(visited_houses_year2)} houses.")
            
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