import re
import json
from os.path import exists
    

PRINT_LENGTH = 60

def getFormattedText(text):
    finalText = []
    
    # Not actually needed? ( let's see... )
    # if len(text) <= PRINT_LENGTH - 2 and not '\n' in text:
    #     finalText.append(text)
    #     return finalText
    
    text = re.findall(r'\S+|\n', text)
    
    listOfWords = []
    for word in text:
        if word == '\n':
            finalText.append(getStringFromListOfWords(listOfWords))
            listOfWords = []
            continue
        
        if len(getStringFromListOfWords(listOfWords + [word])) > PRINT_LENGTH - 2:
            finalText.append(getStringFromListOfWords(listOfWords))
            listOfWords = []
        listOfWords.append(word)
    finalText.append(getStringFromListOfWords(listOfWords))
    
    return finalText

def getStringFromListOfWords(listOfWords) -> str:
    s = ""
    for word in listOfWords:
        s += word + " "
    return s[:-1]

class Day:
    def __init__(self, number: int|str) -> None:
        self.number = int(number)
        self.description = []
        self.result = ""
    
    def set_input(self, path: str) -> None:
        with open(f"{path}/day{self.number}.txt", 'r') as f:
            self.input = f.readlines()
    
    def calculate_output(self) -> None:
        pass # TODO
        
    def set_description(self, description: str|list) -> None:
        if type(description) == list:
            self.description = description
        else:
            self.description = getFormattedText(description)
        
    def set_result(self, result: str|list) -> None:
        if type(result) == list:
            self.result = result
        else:
            self.result = getFormattedText(result)
    
    def __str__(self) -> str:
        s =  "|" + "*"*PRINT_LENGTH + "|\n"
        s +=  "|" + "*" + " "*int(PRINT_LENGTH/2 - 4) + f"DAY {self.number:2d}" + " "*int(PRINT_LENGTH/2 - 4) + "*" + "|\n"
        s +=  "|" + "*"*PRINT_LENGTH + "|\n"
        
        for line in self.description:
            s += "| " + line + " "*(PRINT_LENGTH-len(line) -1 ) + "|\n"
        
        s +=  "|" + "-"*PRINT_LENGTH + "|\n"
        
        for line in self.result:
            s += "| " + line + " "*(PRINT_LENGTH-len(line) -1 ) + "|\n"
            
        s +=  "|" + "*"*PRINT_LENGTH + "|\n"
        
        return s
    
    def append_to_output(self, day_file_path: str) -> None:
        json_file = f"{day_file_path}/../output/out.json"
        
        out = {}
        if exists(json_file):
            with open(json_file, 'r') as f:
                out = json.load(f)
                
        out[f"{self.number}"] = (self.description, self.result)
            
        with open(json_file, 'w') as f:
            json.dump(out, f)

import json

def create_days_from_json(json_file: str) -> list[Day]:
    with open(json_file) as f:
        days_dict = json.load(f)
    
    days = []
    for day_number in days_dict:
        description, result = days_dict[day_number]
        
        day = Day(day_number)
        day.set_description(description)
        day.set_result(result)
        days.append(day)
    
    return days
    

def test_day():
    d1 = Day(2, sorted)
    d2 = Day(23, sorted)
    d1.set_description("This is a short description")
    d1.set_result("This is a short result")
    d2.set_description("This is a very looooong and complicated but definitely awesome description.\n\n It contains many many many words that I hope will cause problems to this script.\n")
    d2.set_result("This is a very looooong and complicated but definitely awesome result. It contains many many many words that I hope will cause problems to this script.")
    print(d1)
    print(d2)
    
    # This prints this (as of commit: Created day.py):
    # |************************************************************|
    # |*                          DAY  2                          *|
    # |************************************************************|
    # | This is a short description                                |
    # |------------------------------------------------------------|
    # | This is a short result                                     |
    # |************************************************************|

    # |************************************************************|
    # |*                          DAY 23                          *|
    # |************************************************************|
    # | This is a very looooong and complicated but definitely     |
    # | awesome description.                                       |
    # |                                                            |
    # | It contains many many many words that I hope will cause    |
    # | problems to this script.                                   |
    # |                                                            |
    # |------------------------------------------------------------|
    # | This is a very looooong and complicated but definitely     |
    # | awesome result. It contains many many many words that I    |
    # | hope will cause problems to this script.                   |
    # |************************************************************| 
    
if __name__ == "__main__":
    test_day()
    
    