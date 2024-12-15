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



class Region:
    def __init__(self, label: str, cells: List[Tuple[int, int]]):
        self.label = label
        self.cells = cells
        self.fences = get_fences(cells)

def get_fences(cells: List[Tuple[int, int]]) -> set[Tuple[Tuple[int, int], Tuple[int, int], str]]:
    fences = set()
    for cell in cells:
        up = (cell[0] - 1, cell[1])
        down = (cell[0] + 1, cell[1])
        left = (cell[0], cell[1] - 1)
        right = (cell[0], cell[1] + 1)
        # up
        if get_chr(up) != get_chr(cell):
            fences.add((cell, up, "H"))
        if get_chr(down) != get_chr(cell):
            fences.add((cell, down, "H"))
        if get_chr(left) != get_chr(cell):
            fences.add((cell, left, "V"))
        if get_chr(right) != get_chr(cell):
            fences.add((cell, right, "V"))

    return fences



def find_sides(fences: set[Tuple[Tuple[int, int], Tuple[int, int], str]]) -> int:
    verticals = [f for f in fences if f[2] == "V"]
    horizontals = [f for f in fences if f[2] == "H"]

    # Connect fences
    sides_count = 0
    while len(horizontals) > 0:
        piece = horizontals.pop()
        side = {piece}
        while True:
            side_len = len(side)
            for f_v in horizontals:
                # Is connected
                for s in side:
                    if ((f_v[0][1] == (s[0][1] + 1) or f_v[0][1] == s[0][1] - 1)
                            and (f_v[0][0] == (s[0][0])) and f_v[1][0] == (s[1][0])):
                        side.add(f_v)
                        break
            if side_len == len(side):
                break

        for s in side:
            if s in horizontals:
                horizontals.remove(s)

        sides_count += 1

    # This went full spaghetti, lots of this duplication could be removed, but i'm done
    while len(verticals) > 0:
        piece = verticals.pop()
        side = {piece}
        while True:
            side_len = len(side)
            for f_v in verticals:
                # Is connected
                for s in side:
                    if ((f_v[0][0] == (s[0][0] + 1) or f_v[0][0] == s[0][0] - 1)
                            and (f_v[0][1] == (s[0][1])) and f_v[1][1] == (s[1][1])):
                        side.add(f_v)
                        break
            if side_len == len(side):
                break

        for s in side:
            if s in verticals:
                verticals.remove(s)

        sides_count += 1



    return sides_count



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
    sides = find_sides(region.fences)
    fence_cost += sides * len(region.cells)
print(fence_cost)

