from collections import deque

rows = []
start_nodes = []
with open('../input_files/day10.txt', 'r') as f:
    lines = f.readlines()
    for r, line in enumerate(lines):
        row = []
        for c, n in enumerate(line.strip()):
            row.append(int(n))
            if int(n) == 0:
                start_nodes.append((r, c))
        rows.append(row)


row_max = len(rows)
col_max = len(rows[0])


def get_neighbors(node: tuple) -> list[tuple]:
    r_idx, c_idx = node
    value = rows[r_idx][c_idx]
    up = (r_idx - 1, c_idx)
    down = (r_idx + 1, c_idx)
    left = (r_idx, c_idx - 1)
    right = (r_idx, c_idx + 1)

    res = []
    for p_neighbor in [up, down, left, right]:
        if (p_neighbor[0] < 0 or p_neighbor[0] >= row_max) or (p_neighbor[1] < 0 or p_neighbor[1] >= col_max):
            continue
        if value + 1 == rows[p_neighbor[0]][p_neighbor[1]]:
            res.append(p_neighbor)

    return res


def get_trail_score(start_node: tuple) -> int:
    q = deque()
    q.append(start_node)
    nine_count = [] # Change this to a set to solve part 1
    while len(q) > 0:
        node = q.pop()
        value = rows[node[0]][node[1]]
        if value == 9:
            nine_count.append(node)
            continue

        neighbors = get_neighbors(node)
        for neighbor in neighbors:
            q.append(neighbor)

    return len(nine_count)


total = 0
for start_n in start_nodes:
    total += get_trail_score(start_n)

print(total)












