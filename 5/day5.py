with open(r'path/to/input.txt', "r") as f:
    input = f.read()

ordering_rules =[split.split("|") for split in [rule for rule in input.split() if len(rule) < 6]]
updates = [number.split(",") for number in [update for update in input.split() if len(update) > 6]]

def rearrange(update : list, rule):
    first = update.index(rule[0])
    second = update.index(rule[1]) 
    update.insert(first, update.pop(second))
    return update

total_part1 = 0
total_part2 = 0

for update in updates:
    update.append(True)
    rearranged = False
    while not rearranged:
        rearranged = True
        for rule in ordering_rules:
            if rule[0] in update and rule[1] in update:
                if update.index(rule[0]) > update.index(rule[1]):
                    rearranged = False
                    update[-1] = False
                    update = rearrange(update, rule)
        
    if update[-1]:
        total_part1 += int(update[(len(update)-2)//2])
    else:
        total_part2 += int(update[(len(update)-2)//2])
print(total_part1)
print(total_part2)