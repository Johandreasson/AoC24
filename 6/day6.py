with open(r'C:\Users\johan\Documents\Python\AoC24\6\input.txt', "r") as f:
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
        print("End of map")

    tile_map, guard_info = update_map(tile_map, guard_info)
    return guard_info


def update_map(tile_map : list, guard_info):
    dir_dict = {"north" : ["^", 0, -1], "east" : [">", 1, 1], "south" : ["v", 0, 1], "west" : ["<", 1, -1]}
    tile_map[guard_info[0]][guard_info[1]] = "x"
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


if __name__ == "__main__":
    input = test
    tiles = [list(row) for row in input]

    
    total = 0
    guard = find_guard(tiles)
    
    while guard[0] in range(len(tiles)) and guard[1] in range(len(tiles[0])):
        guard = patrol(tiles, guard)
        #print_map(tiles)
        #print(guard)

    print(count_tiles(tiles))
