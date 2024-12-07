with open(r'C:\Users\JANDRE21\projects\.vscode\AoC24\6\input.txt', "r") as f:
    input = f.read()

test = ["....#.....",
        ".........#",
        "..........",
        "..#.......",
        ".......#..",
        "..........",
        ".#..^.....",
        "........#.",
        "#.........",
        "......#..."]

input = test

[print(inp) for inp in input]

def find_guard(map):
    for y, row in enumerate(map):
        for x in range(len(row)):
            if map[y][x] == "^":
                 return [y, x, "north"]
            
def patrol(map, guard):
    

def main(map):
    total = 0
    guard = find_guard(map)
    while guard[0] in range(len(map)) and guard[1] in range(len(map[0])):
        guard = patrol(map, guard)

    return total



main(input)