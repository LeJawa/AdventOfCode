from dataclasses import dataclass

with open("inputs/day2.txt", 'r') as f:
    lines = f.readlines()

@dataclass
class Move:   
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

@dataclass
class Result:
    LOSS = 0
    DRAW = 3
    WIN = 6

def moveTranslator(moveInChar: str) -> Move:    
    moveMap = {'A': Move.ROCK, 'B': Move.PAPER, 'C': Move.SCISSORS, 'X': Move.ROCK, 'Y': Move.PAPER, 'Z': Move.SCISSORS}
    
    return moveMap[moveInChar]

def movePredictor(opponentMove: Move, myResultInChar: str) -> Move:
    resultMap = {'X': Result.LOSS, 'Y': Result.DRAW, 'Z': Result.WIN}
    myResult = resultMap[myResultInChar]
    
    if (opponentMove == Move.ROCK and myResult == Result.LOSS) \
        or (opponentMove == Move.PAPER and myResult == Result.WIN) \
            or (opponentMove == Move.SCISSORS and myResult == Result.DRAW):
             return Move.SCISSORS
    if (opponentMove == Move.ROCK and myResult == Result.WIN) \
        or (opponentMove == Move.PAPER and myResult == Result.DRAW) \
            or (opponentMove == Move.SCISSORS and myResult == Result.LOSS):
             return Move.PAPER
    return Move.ROCK

def getRoundScore(opponentMove: Move, myMove: Move) -> Result:    
    if (opponentMove == Move.ROCK and myMove == Move.SCISSORS) \
        or (opponentMove == Move.PAPER and myMove == Move.ROCK) \
            or (opponentMove == Move.SCISSORS and myMove == Move.PAPER):
             return Result.LOSS
    if (opponentMove == Move.ROCK and myMove == Move.PAPER) \
        or (opponentMove == Move.PAPER and myMove == Move.SCISSORS) \
            or (opponentMove == Move.SCISSORS and myMove == Move.ROCK):
             return Result.WIN
    return Result.DRAW

def getFinalScore(opponentMove: Move, myMove: Move) -> int:
    score = myMove + getRoundScore(opponentMove, myMove)
    return score   
    
totalScore1 = 0
totalScore2 = 0

for line in lines:
    opponentMoveInChar, myStrategyInChar = line.split()   
    
    opponentMove = moveTranslator(opponentMoveInChar)
    myMove1 = moveTranslator(myStrategyInChar)
    myMove2 = movePredictor(opponentMove, myStrategyInChar)    
    
    totalScore1 += getFinalScore(opponentMove, myMove1)
    totalScore2 += getFinalScore(opponentMove, myMove2)

print(f"We are playing a Rock-Paper-Scissors tournament with {len(lines)} rounds")
print("---------------------------------------------------------------------------")
print(f"My final score with the first strategy would be: {totalScore1}")
print(f"My final score with the second strategy would be: {totalScore2}")
print("---------------------------------------------------------------------------")