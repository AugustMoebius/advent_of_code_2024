lines = []

with open('../input_files/day04.txt', 'r') as f:
    for line in f:
        lines.append(line.strip())

max_row = len(lines)
max_col = len(lines[0])


down_right = [(-1, 1), (0, 0),  (1, -1)]
down_left = [(-1, -1), (0, 0),  (1, 1)]

directions = [down_right, down_left]


def is_mas(r: int, c: int, direc) -> bool:
    try:
        c1 = (r + direc[0][0], c + direc[0][1])
        c2 = (r + direc[1][0], c + direc[1][1])
        c3 = (r + direc[2][0], c + direc[2][1])

        flattened_list = [item for tup in [c1, c2, c3, ] for item in tup]

        if any(number < 0 for number in flattened_list):
            return False

        l1 = lines[c1[0]][c1[1]]
        l2 = lines[c2[0]][c2[1]]
        l3 = lines[c3[0]][c3[1]]


        word = "".join([l1, l2, l3, ])
        if word == "MAS" or word == "SAM":
            return True

    except IndexError:
        pass
    return False


total_count = 0
for row in range(len(lines)):
    for col in range(len(lines[0])):
        char = lines[row][col]
        if char != "A":
            continue
        is_valid = True
        for direc in directions:
            is_valid = is_valid and is_mas(row, col, direc)

        if is_valid:
            total_count += 1



print(total_count)





