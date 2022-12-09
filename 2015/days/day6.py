from dataclasses import dataclass
from argument_parser import get_config_from_individual_day
import os
import re

from PIL import Image

from day import Day
DAY = 6

@dataclass
class Action:
    Toggle = 0,
    Turn_Off = 1,
    Turn_On = 2,
    Increase_by_one = 3,
    Decrease_by_one = 4,
    Increase_by_two = 5

class Lights:
    def __init__(self) -> None:
        self.n = 1000
        
        self.grid = []
        
        for i in range(self.n):
            self.grid.append([])
            for __ in range(self.n):
                self.grid[i].append(0)
            
        self.max_brightness = 0
    
    def get_coordinates_from_range(self, point1: tuple[int, int], point2: tuple[int, int]) -> list[tuple[int, int]]:
        coordinates:list[tuple[int, int]] = []
        
        for i in range(point1[0], point2[0]+1):
            for j in range(point1[1], point2[1]+1):
                coordinates.append( (i, j) )
        
        return coordinates
    
    def set_point_to(self, point: tuple[int, int], value: int) -> None:
        if value < 0:
            value = 0
        self.grid[point[0]][point[1]] = value
        
    def get_point(self, point: tuple[int, int]) -> int:
        return self.grid[point[0]][point[1]]
    
    def turn_on(self, point1: tuple[int, int], point2: tuple[int, int]) -> None:
        coordinates = self.get_coordinates_from_range(point1, point2)
        
        for coordinate in coordinates:
            self.set_point_to(coordinate, 1)
    
    def turn_off(self, point1: tuple[int, int], point2: tuple[int, int]) -> None:
        coordinates = self.get_coordinates_from_range(point1, point2)
        
        for coordinate in coordinates:
            self.set_point_to(coordinate, 0)
    
    def toggle(self, point1: tuple[int, int], point2: tuple[int, int]) -> None:
        coordinates = self.get_coordinates_from_range(point1, point2)
        
        for coordinate in coordinates:
            if self.get_point(coordinate) == 1:
                self.set_point_to(coordinate, 0)
            else:
                self.set_point_to(coordinate, 1)
    
    def change_brightness(self, point1: tuple[int, int], point2: tuple[int, int], amount: int) -> None:
        coordinates = self.get_coordinates_from_range(point1, point2)
        
        for coordinate in coordinates:
            self.set_point_to(coordinate, self.get_point(coordinate) + amount)
    
    def get_number_of_lights_on(self) -> int:
        count = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.get_point( (i, j) ) > 0:
                    count += 1
        return count

    def get_total_brightness(self) -> int:
        brightness = 0
        for i in range(self.n):
            for j in range(self.n):
                brightness += self.get_point( (i, j) )
        return brightness
    
    def convert_to_rgb(self, point) -> tuple[int, int, int]:
        brightness = self.get_point(point)
        
        rgb_brightness = int(255 * brightness / self.max_brightness)
        
        return rgb_brightness, rgb_brightness, rgb_brightness

    def set_max_brightness(self) -> None:
        self.max_brightness = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.get_point((i,j)) > self.max_brightness:
                    self.max_brightness = self.get_point((i,j))
    
    def show_lights(self) -> None:
        self.set_max_brightness()
        
        im = Image.new(mode="RGB", size=(self.n, self.n))
        pixels = im.load()
        
        for i in range(self.n):
            for j in range(self.n):
                pixels[i,j] = self.convert_to_rgb((i,j))
        
        im.show()
        
                
def parse_instruction(instruction: str) -> tuple[Action, tuple[int, int], tuple[int, int]]:
    
    if instruction.startswith("toggle"):
        action = Action.Toggle
    elif instruction.startswith("turn on"):
        action = Action.Turn_On
    elif instruction.startswith("turn off"):
        action = Action.Turn_Off
        
    points_raw = re.findall(r"(\d+),(\d+) through (\d+),(\d+)", instruction)[0]
    
    return action, (int(points_raw[0]), int(points_raw[1])), (int(points_raw[2]), int(points_raw[3]))
    
def translate_action(action: Action) -> Action:
    if action == Action.Turn_On:
        return Action.Increase_by_one
    elif action == Action.Turn_Off:
        return Action.Decrease_by_one
    elif action == Action.Toggle:
        return Action.Increase_by_two

def run_day(day: Day) -> Day:
    instructions = day.input
    
    lights_part_one = Lights()
    lights_part_two = Lights()
    
    for instruction in instructions:
        action, point1, point2 = parse_instruction(instruction)
        
        translated_action = translate_action(action)
        
        if action == Action.Turn_On:
            lights_part_one.turn_on(point1, point2)
        elif action == Action.Turn_Off:
            lights_part_one.turn_off(point1, point2)
        elif action == Action.Toggle:
            lights_part_one.toggle(point1, point2)
        
        if translated_action == Action.Increase_by_one:
            lights_part_two.change_brightness(point1, point2, 1)
        elif translated_action == Action.Increase_by_two:
            lights_part_two.change_brightness(point1, point2, 2)
        elif translated_action == Action.Decrease_by_one:
            lights_part_two.change_brightness(point1, point2, -1)
    
    # lights_part_one.show_lights()
    # lights_part_two.show_lights()
    
    day.set_description(f"I need to set up my lights by following the {len(instructions)} instructions that Santa has sent me.")
    day.set_result(f"Without translating the instructions, there are a total of {lights_part_one.get_number_of_lights_on()} lights on.\n" \
        + f"After translation of the instructions, the total brightness is {lights_part_two.get_total_brightness()}.")
            
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