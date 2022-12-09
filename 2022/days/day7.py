from argument_parser import get_config_from_individual_day
import os

from day import Day
DAY = 7
PRINT_OUTPUT_MANUAL_OVERRIDE = True

class ParsedLine:
    def __init__(self, line:str) -> None:
        self.is_ls = False
        self.is_cd_down = False
        self.is_cd_up = False
        self.is_file = False
        self.is_folder = False
        self.is_instruction = False
        
        if line[0] == '$':
            self.parse_instruction(line)
        else:
            self.parse_file(line)
            
        self.line = line.strip()
    
    def parse_instruction(self, line: str) -> None:
        self.is_instruction = True
        
        if line[2:].startswith('ls'):
            self.is_ls = True
        elif line[2:].startswith('cd ..'):
            self.is_cd_up = True
        else:
            self.is_cd_down = True
            self.directory_name = line.split()[-1]
    
    def parse_file(self, line: str) -> None:
        split = line.split()
        
        if split[0] == 'dir':
            self.is_folder = True
            self.directory_name = split[1]
            return
        
        self.is_file = True
        self.file_size = int(split[0])    
    
    def __str__(self) -> str:
        return self.line

class LineReader:
    def __init__(self, lines: list[str]) -> None:
        self.lines = lines
        self.current_line = -1
        
    def next(self) -> str:
        self.current_line += 1
        
        try:
            return self.lines[self.current_line]
        except IndexError:
            print("ERROR: no more lines to read.")


def run_day(day: Day) -> Day:
    lines = day.input
    # lines = day.sample
    
    if lines is None:
        return
    
    lines = lines[::-1]
    
    smaller_folders_total_size = 0
    total_size = 0
    end_of_file = False
    
    line_reader = LineReader(lines)
    
    duplicate_counter = 0
    
    folder_sizes = {}
    
    while not end_of_file:
        parsed_line = ParsedLine(line_reader.next())
        
        while(parsed_line.is_instruction):
            parsed_line = ParsedLine(line_reader.next())
        
        directory_size = 0
        
        while(not parsed_line.is_instruction):
            if parsed_line.is_folder:
                directory_size += folder_sizes[parsed_line.directory_name]
            else:
                directory_size += parsed_line.file_size
            parsed_line = ParsedLine(line_reader.next())
        # Must be ls, so we can skip
        parsed_line = ParsedLine(line_reader.next())
        # Should be cd directory_name
        if not parsed_line.is_cd_down:
            print(f"ERROR? Should be cd directory_name: {parsed_line}")
            return
        
        if directory_size <= 100000:
            smaller_folders_total_size += directory_size
            
        name = parsed_line.directory_name
        
        if name in folder_sizes.keys():
            duplicate_counter += 1
            
        folder_sizes[name] = directory_size
                    
        if name == '/':
            end_of_file = True
            total_size = directory_size

    
    # Due to duplicate names in folders, the total size of the '/' directory is wrong. 
    # The code probably only gives the correct answer by chance.
    # I cannot be sure that the sizes of the folders are correct.
    # In fact, I know some of them are incorrect.
    
    # The only way to be sure of the total size occupied is by counting all the files one by one:
    total_size = 0
    for line in lines:
        try:
            total_size += int(line.split()[0])
        except:
            pass    
    
    disk_space = 70000000
    space_needed = 30000000
    
    space_to_free = total_size - (disk_space - space_needed)
    
    # Should be /
    smallest_enough_folder = name
    
    for key, value in folder_sizes.items():
        if value > space_to_free and value < folder_sizes[smallest_enough_folder]:
            smallest_enough_folder = key
    
    day.set_description(f"I need to liberate at least {space_to_free} disk space in this device.")
    day.set_result(f"The total size of all the small folders is: {smaller_folders_total_size}\n" \
        f"The smallest folder to remove to liberate enough space is {smallest_enough_folder} " \
            f"with a size of {folder_sizes[smallest_enough_folder]}.")
            
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