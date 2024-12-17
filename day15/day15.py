from typing import List

map = []
command_list = []


with open('../input_files/day15.txt', 'r') as f:
    is_map = True
    for line in f:
        if line == "\n":
            is_map = False
            continue

        if is_map:
            map.append(line.strip())
        else:
            command_list.append(line.strip())

commands = "".join(command_list)


wall_positions = []
box_positions = []
r_position = None
max_row = len(map)
max_col = len(map[0])

for r_idx, row in enumerate(map):
    for c_idx, val in enumerate(row):
        position = (r_idx, c_idx)
        if val == "#":
            wall_positions.append(position)
        elif val == "O":
            box_positions.append(position)
        elif val == "@":
            r_position = position

def update_box(box_position: tuple[int, int], direction: chr) -> bool:
    new_box_pos = None
    match direction:
        case "^":
            for i in range(box_position[0], -1, -1):
                temp_pos = (i, box_position[1])
                if temp_pos in wall_positions:
                    break
                if temp_pos not in box_positions:
                    new_box_pos = temp_pos
                    break
        case "v":
            for i in range(box_position[0], max_row):
                temp_pos = (i, box_position[1])
                if temp_pos in wall_positions:
                    break
                if temp_pos not in box_positions:
                    new_box_pos = temp_pos
                    break
        case ">":
            for i in range(box_position[1], max_col):
                temp_pos = (box_position[0], i)
                if temp_pos in wall_positions:
                    break
                if temp_pos not in box_positions:
                    new_box_pos = temp_pos
                    break
        case "<":
            for i in range(box_position[1], -1, -1):
                temp_pos = (box_position[0], i)
                if temp_pos in wall_positions:
                    break
                if temp_pos not in box_positions:
                    new_box_pos = temp_pos
                    break

    if not new_box_pos:
        return False

    box_positions.remove(box_position)
    box_positions.append(new_box_pos)
    return True


def try_move(new_robot_pos: tuple[int, int]) -> bool:
    if new_robot_pos in wall_positions:
        return False
    if new_robot_pos in box_positions:
        if not update_box(new_robot_pos, command):
            # Cant move
            return False
    return True


for command in commands:
    match command:
        case "^":
            new_pos = (r_position[0] - 1, r_position[1])
            if try_move(new_pos):
                r_position = new_pos
        case "v":
            new_pos = (r_position[0] + 1, r_position[1])
            if try_move(new_pos):
                r_position = new_pos
        case ">":
            new_pos = (r_position[0], r_position[1] + 1)
            if try_move(new_pos):
                r_position = new_pos
        case "<":
            new_pos = (r_position[0], r_position[1] - 1)
            if try_move(new_pos):
                r_position = new_pos




total = 0
for box in box_positions:
    total += 100 * box[0] + box[1]


print(total)