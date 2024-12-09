with open(r'C:\Users\JANDRE21\Repos\AoC24\6\input.txt', "r") as f:
    input = f.read().splitlines()

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

def find_guard(tile_map):
    for y, row in enumerate(tile_map):
        for x, tile in enumerate(row):
            if tile == "^":
                 return [y, x, "north"]


def patrol(tile_map : list, guard_info, mark = True):
    try:
        if guard_info[2] == "north" and tile_map[guard_info[0]-1][guard_info[1]] == "#":
            guard_info[2] = "east"
            tile_map[guard_info[0]][guard_info[1]] = ">"
        elif guard_info[2] == "east" and tile_map[guard_info[0]][guard_info[1]+1] == "#":
            guard_info[2] = "south"
            tile_map[guard_info[0]][guard_info[1]] = "v"
        elif guard_info[2] == "south" and tile_map[guard_info[0]+1][guard_info[1]] == "#":
            guard_info[2] = "west"
            tile_map[guard_info[0]][guard_info[1]] = "<"
        elif guard_info[2] == "west" and tile_map[guard_info[0]][guard_info[1]-1] == "#":
            guard_info[2] = "north"
            tile_map[guard_info[0]][guard_info[1]] = "^"
    except IndexError:
        pass

    tile_map, guard_info = update_map(tile_map, guard_info, mark)
    return guard_info


def update_map(tile_map : list, guard_info, mark=True):
    dir_dict = {"north" : ["^", 0, -1], "east" : [">", 1, 1], "south" : ["v", 0, 1], "west" : ["<", 1, -1]}
    if mark:
        tile_map[guard_info[0]][guard_info[1]] = "x" 
    else:
        tile_map[guard_info[0]][guard_info[1]] = "."
    guard_info[dir_dict[guard_info[2]][1]] += dir_dict[guard_info[2]][2]
    if guard_info[0] in range(len(tile_map)) and guard_info[1] in range(len(tile_map[0])):
        tile_map[guard_info[0]][guard_info[1]] = dir_dict[guard_info[2]][0]
    return tile_map, guard_info


def count_tiles(tile_map):
    tiles = 0
    for row in tile_map:
        for tile in row:
            if tile == "x":
                tiles += 1
    return tiles


def print_map(tile_map):
    for row in tile_map:
        [print(tile, end=" ") for tile in row]
        print("\n")
    print()

def part1(tile_map, guard_info):
    while guard_info[0] in range(len(tiles)) and guard_info[1] in range(len(tiles[0])):
        guard_info = patrol(tiles, guard_info)
        #print_map(tiles)
        #print(guard)
    return count_tiles(tile_map)

def part2(inp, guard_start):
    total = 0
    for y, row in enumerate(inp):
        for x, tile in enumerate(row):
            tiles = [list(row) for row in inp]
            guard_info = [info for info in guard_start]
            if tile != "#":
                tiles[y][x] = "#"
                
                guard_history = []
                i = 0
                while guard_info[0] in range(len(tiles)) and guard_info[1] in range(len(tiles[0])):
                    guard_info = patrol(tiles, guard_info, False)
                    #print_map(tiles)
                    i += 1
                    if i > 50:
                        total += 1
                        break
    return total

if __name__ == "__main__":
    input = test
    tiles = [list(row) for row in input]

    guard = find_guard(tiles)
    #part1(tiles, guard)
    print(part2(input, guard))