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


def patrol(tile_map : list, guard_info):
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

    tile_map, guard_info, new_x = update_map(tile_map, guard_info)
    return guard_info, new_x


def update_map(tile_map : list, guard_info):
    dir_dict = {"north" : ["^", 0, -1], "east" : [">", 1, 1], "south" : ["v", 0, 1], "west" : ["<", 1, -1]}
    new_x = False
    tile_map[guard_info[0]][guard_info[1]] = "x" 
    guard_info[dir_dict[guard_info[2]][1]] += dir_dict[guard_info[2]][2]
    if guard_info[0] in range(len(tile_map)) and guard_info[1] in range(len(tile_map[0])):
        if tile_map[guard_info[0]][guard_info[1]] != "x":
            new_x = True
        tile_map[guard_info[0]][guard_info[1]] = dir_dict[guard_info[2]][0]
    return tile_map, guard_info, new_x


def count_tiles(tile_map):
    tiles = 0
    for row in tile_map:
        tiles += row.count("x")
    return tiles


def print_map(tile_map):
    for row in tile_map:
        [print(tile, end=" ") for tile in row]
        print("\n")
    print()


def part1(tile_map, guard_info):
    while guard_info[0] in range(len(tiles)) and guard_info[1] in range(len(tiles[0])):
        guard_info, _ = patrol(tiles, guard_info)
        #print_map(tiles)
        #print(guard)
    return count_tiles(tile_map)


def part2(inp, guard_start):
    total = 0
    for y, row in enumerate(inp):
        print(y)
        for x, tile in enumerate(row):
            if tile == "x" and tile != "#":
                guard_info = [info for info in guard_start]
                tiles2 = [list(row) for row in input]
                tiles2[y][x] = "#"
                no_x_streak = 0
                while guard_info[0] in range(len(tiles2)) and guard_info[1] in range(len(tiles2[0])):
                    guard_info, new_x = patrol(tiles2, guard_info)
                    #print_map(tiles)
                    if new_x:
                        no_x_streak = 0
                    else:
                        no_x_streak += 1
                    if no_x_streak > 5000:
                        total += 1
                        break

    return total

if __name__ == "__main__":
    #input = test
    tiles = [list(row) for row in input]
    guard = find_guard(tiles)
    guard2 = find_guard(tiles)
    print(part1(tiles, guard))
    print(part2(tiles, guard2))