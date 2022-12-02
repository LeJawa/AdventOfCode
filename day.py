import re

PRINT_LENGTH = 60

def getFormattedText(text):
    finalText = []
    
    if len(text) <= PRINT_LENGTH - 2:
        finalText.append(text)
        return finalText
    
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
    def __init__(self, number, solution_function) -> None:
        self.number = number
        self.solution_function = solution_function
        self.description = []
        self.result = ""
        
    def set_description(self, description: str) -> None:
        self.description = getFormattedText(description)
        
    def set_result(self, result: str) -> None:
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
    
    