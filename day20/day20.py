from collections import deque
from typing import List

rows = []

with open('../input_files/day20.txt', 'r') as f:
    for line in f:
        rows.append(line.strip())

max_row = len(rows)
max_col = len(rows[0])
initial_wall_positions = set()
initial_position = None
goal = None

for row_idx, row in enumerate(rows):
    for col_idx, col in enumerate(row):
        if col == "#":
            initial_wall_positions.add((row_idx, col_idx))
        if col == "S":
            initial_position = (row_idx, col_idx)
        if col == "E":
            goal = (row_idx, col_idx)

class State:
    def __init__(self, position: tuple[int, int], parent: 'State' = None):
        self.position = position
        self.parent = parent
        self.hash = None


    def get_path(self):
        path = []
        current = self
        while current is not None:
            path.append(current.position)
            current = current.parent
        return path

    def __eq__(self, other: 'State') -> bool:
        return self.position == other.position

    def __hash__(self) -> int:
        if self.hash is None:
            self.hash = hash(self.position)
        return self.hash

    def __repr__(self):
        return f"State({self.position})"

class Path:
    def __init__(self, path: List[tuple[int, int]]):
        self.path = path

    def __eq__(self, other: 'Path') -> bool:
        return self.path == other.path

    def __hash__(self) -> int:
        return hash(tuple(self.path))

    def __repr__(self):
        return f"Path({self.path})"



def find_path_length(start: tuple[int, int], wall_positions: set[tuple[int, int]]) -> Path:
    q = deque()
    q_set = set()
    visited = set()

    start_state = State(position=start)
    q.append(start_state)
    q_set.add(start_state)

    while len(q) > 0:
        current = q.popleft()
        q_set.remove(current)
        visited.add(current)

        if current.position == goal:
            # Get len
            return Path(current.get_path())

        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor_position = (current.position[0] + direction[0], current.position[1] + direction[1])
            if not (0 < neighbor_position[0] < max_row or 0 < neighbor_position[1] < max_col):
                continue
            new_state = State(neighbor_position, current)
            if neighbor_position not in wall_positions and new_state not in visited and new_state not in q_set:
                q.append(new_state)
                q_set.add(new_state)





# Find all pairs of touching walls
touching_walls = set()
for wall in initial_wall_positions:
    for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        neighbor = (wall[0] + direction[0], wall[1] + direction[1])
        if neighbor in initial_wall_positions and (neighbor, wall) not in touching_walls:
            touching_walls.add((wall, neighbor))

base_line = len(find_path_length(initial_position, initial_wall_positions).path)
saved_dict = {}

paths = set()
for w_positions in touching_walls:
    truncated_walls = initial_wall_positions.copy()
    truncated_walls.remove(w_positions[0])
    truncated_walls.remove(w_positions[1])
    paths.add(find_path_length(initial_position, truncated_walls))


for path in paths:
    time_saved = base_line - len(path.path)
    if time_saved < base_line:
        if time_saved > 0:
            saved_dict[time_saved] = saved_dict.get(time_saved, 0) + 1




print()
