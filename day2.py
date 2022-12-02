with open("inputs/day2.txt", 'r') as f:
    lines = f.readlines()
    
ROCK = 1
PAPER = 2
SCISSORS = 4
WIN = 6
LOSS = 0
DRAW = 3


def getRoundScore(opponentMove, myMove):
    
    if myMove in [WIN, LOSS, DRAW]:
        return myMove
    
    if (opponentMove == ROCK and myMove == SCISSORS) \
        or (opponentMove == PAPER and myMove == ROCK) \
            or (opponentMove == SCISSORS and myMove == PAPER):
             return LOSS
    if (opponentMove == ROCK and myMove == PAPER) \
        or (opponentMove == PAPER and myMove == SCISSORS) \
            or (opponentMove == SCISSORS and myMove == ROCK):
             return WIN
    return DRAW

def moveTranslator(moveInChar):    
    moveMap = {'A': ROCK, 'B': PAPER, 'C': SCISSORS, 'X': ROCK, 'Y': PAPER, 'Z': SCISSORS}
    
    return moveMap[moveInChar]
    
def movePredictor(opponentMove, myResultInChar):
    resultMap = {'X': LOSS, 'Y': DRAW, 'Z': WIN}
    myResult = resultMap[myResultInChar]
    
    if (opponentMove == ROCK and myResult == LOSS) \
        or (opponentMove == PAPER and myResult == WIN) \
            or (opponentMove == SCISSORS and myResult == DRAW):
             return SCISSORS
    if (opponentMove == ROCK and myResult == WIN) \
        or (opponentMove == PAPER and myResult == DRAW) \
            or (opponentMove == SCISSORS and myResult == LOSS):
             return PAPER
    return ROCK
    
    


def getScore(opponentMove, myMove):
    score = 0
    if myMove == ROCK:
        score += 1
    elif myMove == PAPER:
        score += 2
    elif myMove == SCISSORS:
        score += 3
    else:
        print(f"myMove not recognized: {myMove}")
    
    score += getRoundScore(opponentMove, myMove)
    return score   
    
    
totalScore1 = 0
totalScore2 = 0

for line in lines:
    opponentMoveInChar, myMoveInChar = line.split()   
    
    opponentMove = moveTranslator(opponentMoveInChar)
    myMove1 = moveTranslator(myMoveInChar)
    myMove2 = movePredictor(opponentMove, myMoveInChar)    
    
    totalScore1 += getScore(opponentMove, myMove1)
    totalScore2 += getScore(opponentMove, myMove2)

print(f"My final score with the first strategy is {totalScore1}")
print(f"My final score with the second strategy is {totalScore2}")