from argument_parser import get_config_from_individual_day
import os

from day import Day
DAY = 2

def perimeter(dimensions: list[int]) -> int:
    return 2*(dimensions[0] + dimensions[1])

def surface(dimensions: list[int]) -> int:
    return dimensions[0] * dimensions[1]

def volume(dimensions: list[int]) -> int:
    return dimensions[0]*dimensions[1]*dimensions[2]

def wrapping_surface(dimensions: list[int]) -> int:
    return 2*surface(dimensions[0:2]) + 2*surface(dimensions[0:3:2]) + 2*surface(dimensions[1:3])

def smaller_side_surface(dimensions: list[int]) -> int:
    return min([surface(dimensions[0:2]), surface(dimensions[0:3:2]), surface(dimensions[1:3])])

def smaller_side_perimeter(dimensions: list[int]) -> int:
    return min([perimeter(dimensions[0:2]), perimeter(dimensions[0:3:2]), perimeter(dimensions[1:3])])


def run_day(day: Day) -> Day:
    dimensions = day.input
    
    paper_wrap_needed = 0
    ribbon_needed = 0
    
    for dimension in dimensions:
        dims = [int(i) for i in dimension.strip().split(sep='x')]
        
        paper_wrap_needed += wrapping_surface(dims) + smaller_side_surface(dims)
        ribbon_needed += volume(dims) + smaller_side_perimeter(dims)
    
    day.set_description(f"The elves are wrapping {len(dimensions)} gifts but need to order the wrapping paper.")
    day.set_result(f"To exactly wrap the gifts, they need to order {paper_wrap_needed} square feet of paper wrap and {ribbon_needed} feet of ribbon.")
            
    return day


if __name__ == "__main__":
    
    PATH = os.path.dirname(__file__)
    
    config = get_config()

    PRINT_OUTPUT = not config['no_output']
        
    day = Day(DAY)
    day.set_input(f"{PATH}/../input/")
    day = run_day(day)
    day.append_to_output(PATH)
    
    if PRINT_OUTPUT:
        print(day)