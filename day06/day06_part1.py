from enum import Enum

rows = []
with open('../input_files/day06.txt', 'r') as f:
    for line in f:
        rows.append(line.strip())

max_row = len(rows)
max_col = len(rows[0])

start_pos = None

for r in range(max_row):
    for c in range(max_col):
        if rows[r][c] == "^":
            start_pos = (r, c)
            break


class Dir(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


dif_map = {
    Dir.NORTH: (-1, 0),
    Dir.SOUTH: (1, 0),
    Dir.EAST: (0, 1),
    Dir.WEST: (0, -1)
}


current_dir = Dir.NORTH
current_pos = start_pos
path = [start_pos]

while True:
    dif = dif_map[current_dir]
    next_pos = (current_pos[0] + dif[0], current_pos[1] + dif[1])
    if next_pos[0] >= max_row or next_pos[1] >= max_col:
        break

    if rows[next_pos[0]][next_pos[1]] == "#":
        current_dir = Dir((current_dir.value + 1) % 4)
        continue

    current_pos = next_pos
    path.append(current_pos)

print(len(set(path)))





