from day import Day

DAY_NUMBER = 1

def get_description_and_result() -> tuple[str, str]:
    with open("inputs/day1.txt", 'r') as f:
        lines = f.readlines()

    caloriesPerElf = []
    elfCalories = 0

    for line in lines:
        line = line.strip()
        if line == '':
            caloriesPerElf.append(elfCalories)
            elfCalories = 0
            continue
    
        elfCalories += int(line)

    # This is really clever.
    # First element is a list from 0 to NumberOfElves, i.e. length of caloriesPerElf.
    # Second element is the key which converts each element of the first list into its corresponding calories.
    # reverse is just to get descending ordering.
    # sorted will then sort the first list as if it contained the calories given by the key.
    # The final list will not contain the calories, but the numbers from 0 to NumberOfElves.
    orderedListOfElves = sorted(list(range(len(caloriesPerElf))), key = lambda i: caloriesPerElf[i], reverse=True)
    orderedListOfCalories = [caloriesPerElf[elf] for elf in orderedListOfElves]
    
    description = f"In the jungle there are {len(caloriesPerElf)} elves carrying calories."
    result = f"Elf #{orderedListOfElves[0]} is carrying the most calories: {orderedListOfCalories[0]}\n\n" \
            + f"The top three elves carrying calories are: elf #{orderedListOfElves[0]}, elf #{orderedListOfElves[1]} and elf #{orderedListOfElves[2]}\n" \
            + f"They are carrying a total of {sum(orderedListOfCalories[:3])} calories" 
            
    return description, result
    
def main() -> None:
    description, result = get_description_and_result()
    print(description)
    print("---------------------------------------------------------------------------")
    print(result)
    print("---------------------------------------------------------------------------")

def getDay() -> Day:
    description, result = get_description_and_result()
    
    day = Day(DAY_NUMBER)
    day.set_description(description)
    day.set_result(result)
    
    return day

if __name__ == "__main__":
    main()