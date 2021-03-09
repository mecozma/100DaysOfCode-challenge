"""
You start on the open square (.) in the top-left corner and need to reach the
bottom (below the bottom-most row on your map).
The toboggan can only follow a few specific slopes (you opted for a cheaper
model that prefers rational numbers); start by counting all the trees you would
encounter for the slope right 3, down 1:
From your starting position at the top-left, check the position that is right 3
and down 1. Then, check the position that is right 3 and down 1 from there, and
so on until you go past the bottom of the map.
The locations you'd check in the above example are marked here with O where
there was an open square and X where there was a tree:

..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
In this example, traversing the map using this slope would cause you to
encounter 7 trees.

Starting at the top-left corner of your map and following a slope of right 3
and down 1, how many trees would you encounter?
"""


slopes_file = 'input.txt'


# Rread the input file.
with open(slopes_file, 'r') as f:
    input_data = [line.strip() for line in f]

# The slope used by the elf.
slope = [3, 1]


# Traverse slope.
def part_1(data):
    slope_width = len(data[0])
    slope_height = len(data)
    jump = 0
    tree = '#'
    trees = 0

    for line in range(slope_height):
        if data[line][jump] == tree:
            trees += 1
        jump = (jump + 3) % slope_width
    return trees


print(f'Nr. trees Part 1: {part_1(input_data)}')

# Part two.

# A collection of the slopes to iterate over.
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]


def part_two(data, slopes):
    trees_product = 1

    def traverse_slopes(slopes):
        slope_width = len(data[0])
        slope_height = len(data)
        jump = 0
        tree = '#'
        trees = 0
        right = slopes[0]
        down = slopes[1]
        for line in range(slope_height):
            if line % down != 0:
                continue
            if data[line][jump] == tree:
                trees += 1
            jump = (jump + right) % slope_width
        return trees
    for slope in slopes:
        trees_product *= traverse_slopes(slope)
    return trees_product


print(f'Nr. trees Part 2: {part_two(input_data, slopes)}')
