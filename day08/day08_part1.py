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




def get_antinode_pos(a1: tuple, a2: tuple) -> tuple:
    row_dif = a1[0] - a2[0]
    col_dif = a1[1] - a2[1]
    return a1[0] + row_dif, a1[1] + col_dif


def is_in_map(pos: tuple) -> bool:
    return 0 <= pos[0] < row_max and 0 <= pos[1] < row_max


antinode_positions = []

for positions in antennas.values():
    for a1 in positions:
        for a2 in positions:
            if a1 == a2:
                continue
            antinode_positions.append(get_antinode_pos(a1, a2))

valid = {p for p in antinode_positions if is_in_map(p)}
print(len(valid))



