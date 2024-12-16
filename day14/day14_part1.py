# max_col = 11
# max_row = 7
#
max_col = 101
max_row = 103


class Robot:
    def __init__(self, position: tuple[int, int], velocity: tuple[int, int]):
        self.position = position
        self.velocity = velocity

    def move(self, seconds):
        row_pos = (self.position[0] + self.velocity[0] * seconds) % max_row
        col_pos = (self.position[1] + self.velocity[1] * seconds) % max_col
        self.position = (row_pos, col_pos)


robots = []
with open('../input_files/day14.txt', 'r') as f:
    for line in f:
        split1 = line.strip().split(" ")
        split2 = [s.split("=")[1] for s in split1]
        pos = split2[0].split(",")
        vel = split2[1].split(",")

        robots.append(Robot(
            position=(int(pos[1]), int(pos[0])),
            velocity=(int(vel[1]), int(vel[0]))
        ))

print()


for robot in robots:
    robot.move(100)


middle_row = max_row // 2
middle_col = max_col // 2

top_left_count = 0
top_right_count = 0
bottom_left_count = 0
bottom_right_count = 0

for robot in robots:
    r_row = robot.position[0]
    r_col = robot.position[1]
    # top left
    if r_row < middle_row and r_col < middle_col:
        top_left_count += 1
    # top right
    if r_row < middle_row and r_col > middle_col:
        top_right_count += 1
    # bottom left
    if r_row > middle_row and r_col < middle_col:
        bottom_left_count += 1
    # bottom right
    if r_row > middle_row and r_col > middle_col:
        bottom_right_count += 1

print(top_left_count * top_right_count * bottom_left_count * bottom_right_count)