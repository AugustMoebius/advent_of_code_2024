from typing import List

rows = []
with open('../input_files/day08.txt', 'r') as f:
    for line in f:
        rows.append(line.strip())

row_max = len(rows)
col_max = len(rows[0])
antennas = {}
antenna_positions = set()
for i_row, row in enumerate(rows):
    for i_col, symbol in enumerate(row):
        if symbol == ".":
            continue
        position = (i_row, i_col)
        antennas.setdefault(symbol, []).append(position)
        antenna_positions.add(position)


def is_in_map(pos: tuple) -> bool:
    return 0 <= pos[0] < row_max and 0 <= pos[1] < row_max


def get_antinode_positions(a1: tuple, a2: tuple) -> set[tuple]:
    node_positions = {a1, a2}
    source_node = a1
    mirror_node = a2
    while True:
        row_dif = mirror_node[0] - source_node[0]
        col_dif = mirror_node[1] - source_node[1]
        new_pos = (mirror_node[0] + row_dif, mirror_node[1] + col_dif)
        if not is_in_map(new_pos):
            break
        node_positions.add(new_pos)
        source_node = mirror_node
        mirror_node = new_pos

    return node_positions

antinode_positions = set()

for positions in antennas.values():
    for a1 in positions:
        for a2 in positions:
            if a1 == a2:
                continue
            antinode_positions = antinode_positions.union(get_antinode_positions(a1, a2))

print(len(antinode_positions))



