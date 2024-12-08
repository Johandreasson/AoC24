import re

with open(r'path/to/input.txt', "r") as f:
    memory = f.read()

    multiples = re.findall(r'(mul\(\d+,\d+\)|do\(\)|don\'t\(\))', memory)

    total = 0
    enabled = True
    for multiple in multiples:
        if multiple == "do()":
            enabled = True
        elif multiple == "don't()":
            enabled = False
        if "mul" in multiple and enabled:
            total += int(multiple[3:].strip("()").split(",")[0]) * int(multiple[3:].strip("()").split(",")[1])
            

    print(total)