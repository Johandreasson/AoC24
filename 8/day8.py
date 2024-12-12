with open(r'C:\Users\JANDRE21\Repos\AoC24\8\input.txt', "r") as f:
    input = f.read().splitlines()

test="""............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""
""" Expected result:
......#....#
...#....0...
....#0....#.
..#....0....
....0....#..
.#....A.....
...#........
#......#....
........A...
.........A..
..........#.
..........#."""

def find_antennas(tilemap):
    antennas = {}
    for i, row in enumerate(tilemap):
        for j, tile in enumerate(row):
            if tile == ".":
                continue
            if tile not in antennas.keys():
                antennas[tile] = []
            antennas[tile].append((i,j))
    return antennas

def part1(tilemap):
    antennas = find_antennas(tilemap)
    unique = set()

    print(antennas)
    for antenna in antennas.items():
        #print(antenna[0])
        for i, location in enumerate(antenna[1]):
            for j in range(i, len(antenna[1])-1):
                #print(location, "-", antenna[1][j+1])
                delta_y = abs(location[0]-antenna[1][j+1][0])
                delta_x = abs(location[1]-antenna[1][j+1][1])
                if location[0]+delta_y <= len(tilemap)-1 and location[1]+delta_x <= len(tilemap[0])-1:
                    print(location[0]+delta_y, location[1]+delta_x)
                    unique.add((location[0]+delta_y, location[1]+delta_x))

                if location[0]-delta_y >= 0 and location[1]-delta_x >= 0:
                    print(location[0]-delta_y, location[1]-delta_x)
                    unique.add((location[0]-delta_y, location[1]-delta_x))

                #print(, "-", location, "-", antenna[1][j+1], (location[0]+delta_y, location[1]+delta_x))
                #if something:
                #    valid_pairs.append(location, antenna[1][j+1])
            #print()
    print(unique)
    return len(unique)

def part2():
    pass

if __name__ == "__main__":
    input = test.splitlines()
    input = [list(row) for row in input]
    
    print(part1(input))