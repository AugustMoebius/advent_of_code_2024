import time
from enum import Enum

rows = []
with open('../input_files/day06.txt', 'r') as f:
    for line in f:
        rows.append(line.strip())

max_row = len(rows)
max_col = len(rows[0])

start_pos = None
wall_pos = set()

for r in range(max_row):
    for c in range(max_col):
        if rows[r][c] == "^":
            start_pos = (r, c)
        if rows[r][c] == "#":
            wall_pos.add((r, c))


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


def is_loop(wall_positions: set[tuple]) -> bool:
    current_dir = Dir.NORTH
    current_pos = start_pos
    dir_array = [[None for _ in range(max_col)] for _ in range(max_row)]
    dir_array[current_pos[0]][current_pos[1]] = current_dir
    while True:
        dif = dif_map[current_dir]
        next_pos = (current_pos[0] + dif[0], current_pos[1] + dif[1])

        if (next_pos[0] >= max_row or next_pos[1] >= max_col
                or next_pos[0] < 0 or next_pos[1] < 0):
            break

        if next_pos in wall_positions:
            current_dir = Dir((current_dir.value + 1) % 4)
            continue

        current_pos = next_pos

        if dir_array[current_pos[0]][current_pos[1]] == current_dir:
            return True
        dir_array[current_pos[0]][current_pos[1]] = current_dir

    return False

start_time = time.time()
loop_count = 0
for r in range(max_row):
    print(r)
    for c in range(max_col):
        pos = (r, c)
        if pos in wall_pos or pos == start_pos:
            continue
        if is_loop({pos}.union(wall_pos)):
            loop_count += 1

# Record end time
end_time = time.time()

# Calculate and print the elapsed time
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")

print(loop_count)
