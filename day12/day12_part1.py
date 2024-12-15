from collections import deque
from typing import List

rows = []
with open('../input_files/day12.txt', 'r') as f:
    for line in f:
        rows.append(line.strip())

row_max = len(rows)
col_max = len(rows[0])


def get_chr(cell: tuple):
    row = cell[0]
    col = cell[1]
    if 0 <= row < row_max and 0 <= col < col_max:
        return rows[row][col]
    return None


from typing import List, Tuple

class Region:
    def __init__(self, label: str, cells: List[Tuple[int, int]]):
        self.label = label
        self.cells = cells


def get_neighbors(cell: Tuple[int, int]) -> list[Tuple[int, int]]:
    # up
    neighbors = []
    if cell[0] - 1 >= 0:
        neighbors.append((cell[0] - 1, cell[1]))
    # down
    if cell[0] + 1 < row_max:
        neighbors.append((cell[0] + 1, cell[1]))
    # left
    if cell[1] - 1 >= 0:
        neighbors.append((cell[0], cell[1] - 1))
    # right
    if cell[1] + 1 < col_max:
        neighbors.append((cell[0], cell[1] + 1))

    return [x for x in neighbors if get_chr(x) == get_chr(cell)]


def find_region_cells(start: tuple) -> set[Tuple[int, int]]:
    q = deque([start])
    q_set = set()
    q_set.add(start)
    visited = set()
    label = rows[start[0]][start[1]]
    while len(q) > 0:
        cell = q.popleft()
        q_set.remove(cell)
        visited.add(cell)

        neighbors = get_neighbors(cell)

        for n in neighbors:
            if n not in visited and n not in q_set:
                q.append(n)
                q_set.add(n)

    return visited


def find_regions() -> List[Region]:
    regions = []
    visited = set()
    for r, row in enumerate(rows):
        for c, col in enumerate(row):
            cell = (r, c)
            if cell not in visited:
                region_cells = find_region_cells(cell)
                regions.append(Region(label=get_chr(cell), cells=region_cells))
                visited = visited.union(region_cells)

    return regions


regions = find_regions()

fence_cost = 0

for region in regions:
    fence_count = 0
    for cell in region.cells:
        neighbor_count = len(get_neighbors(cell))
        if neighbor_count == 0:
            fence_count += 4
        elif neighbor_count == 1:
            fence_count += 3
        elif neighbor_count == 2:
            fence_count += 2
        elif neighbor_count == 3:
            fence_count += 1

    fence_cost += fence_count * len(region.cells)

print(fence_cost)
