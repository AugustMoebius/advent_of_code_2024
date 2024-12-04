lines = []

with open('../input_files/day04.txt', 'r') as f:
    for line in f:
        lines.append(line.strip())

max_row = len(lines)
max_col = len(lines[0])

up = [(0, 0), (0, 1), (0, 2), (0, 3)]
down = [(0, 0), (0, -1), (0, -2), (0, -3)]
right = [(0, 0), (1, 0), (2, 0), (3, 0)]
left = [(0, 0), (-1, 0), (-2, 0), (-3, 0)]

up_right = [(0, 0), (1, 1), (2, 2), (3, 3)]
up_left = [(0, 0), (-1, 1), (-2, 2), (-3, 3)]
down_right = [(0, 0), (1, -1), (2, -2), (3, -3)]
down_left = [(0, 0), (-1, -1), (-2, -2), (-3, -3)]

directions = [up, down, right, left, up_right, up_left, down_right, down_left]


def is_xmas(r: int, c: int, direc) -> bool:
    try:
        c1 = (r + direc[0][0], c + direc[0][1])
        c2 = (r + direc[1][0], c + direc[1][1])
        c3 = (r + direc[2][0], c + direc[2][1])
        c4 = (r + direc[3][0], c + direc[3][1])

        flattened_list = [item for tup in [c1, c2, c3, c4] for item in tup]

        if any(number < 0 for number in flattened_list):
            return False

        l1 = lines[c1[0]][c1[1]]
        l2 = lines[c2[0]][c2[1]]
        l3 = lines[c3[0]][c3[1]]
        l4 = lines[c4[0]][c4[1]]

        word = "".join([l1, l2, l3, l4])
        if word == "XMAS":
            return True

    except IndexError:
        pass
    return False


total_count = 0
for row in range(len(lines)):
    for col in range(len(lines[0])):
        char = lines[row][col]
        if char != "X":
            continue
        for direc in directions:
            if is_xmas(row, col, direc):
                total_count += 1


print(total_count)





