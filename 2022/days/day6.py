from argument_parser import get_config_from_individual_day
import os

from day import Day
DAY = 6

class MarkerFinder:
    def __init__(self, marker_length) -> None:
        self.characters = []
        self.marker_length = marker_length

    def next_char(self, character: str) -> None:        
        if len(self.characters) < self.marker_length:
            self.characters.append(character)            
            return
            
        for i in range(self.marker_length - 1):
            self.characters[i] = self.characters[i+1]
        self.characters[-1] = character
   
    def is_marker(self) -> bool:
        if len(self.characters) < self.marker_length:
            return False
        
        return len(list(dict.fromkeys(self.characters))) == len(self.characters)

def run_day(day: Day) -> Day:
    buffer = day.input[0]
    
    start_marker_finder = MarkerFinder(4)
    message_marker_finder = MarkerFinder(14)
    start_of_packet = -1
    start_of_message = -1
    
    for i in range(len(buffer)):
        if start_of_packet != -1 and start_of_message != -1:
            break
        
        if start_of_packet == -1 and start_marker_finder.is_marker():
            start_of_packet = i
            
        if start_of_message == -1 and message_marker_finder.is_marker():
            start_of_message = i
            
        start_marker_finder.next_char(buffer[i])
        message_marker_finder.next_char(buffer[i])
    
    if start_of_packet == -1:
        print('Error: start of packet marker not found!')
    if start_of_message == -1:
        print('Error: start of message marker not found!')
        
    day.set_description(f"I am trying to find start of packet and start of message markers on a buffer of length {len(buffer)}.")
    day.set_result(f"The start of packet marker is found at the {start_of_packet}th position.\nThe start of message marker is found at the {start_of_message}th position.")
            
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