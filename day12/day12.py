from collections import deque
from typing import List

rows = []
with open('../input_files/day11.txt', 'r') as f:
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


class Region:
    def __int__(self, label: chr, cells: List[tuple]):
        self.label = label
        self.cells = cells


def find_region_cells(start: tuple):
    q = deque([start])
    visited = set()
    label = rows[start[0]][start[1]]
    while len(q) > 0:
        cell = q.popleft()
        visited.add(cell)







