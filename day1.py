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

maxCalories = 0
elfIndex = 0

for i in range(len(caloriesPerElf)):
    if caloriesPerElf[i] > maxCalories:
        maxCalories = caloriesPerElf[i]
        elfIndex = i

print(f"Elf #{elfIndex} is carrying the most calories ({maxCalories})")

print(f"The top three elves carrying calories are carrying a total of {sum(sorted(caloriesPerElf)[-3:])} calories")
        