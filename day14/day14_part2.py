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


def print_robots():
    robot_positions = {r.position for r in robots}

    for r_idx in range(max_row):
        line = []
        for c_idx in range(max_col):
            if (r_idx, c_idx) in robot_positions:
                line.append("🟩")  # White square for robot position
            else:
                line.append("⬛")  # Green square for empty position

        print("".join(line))


for i in range(10000):
    for robot in robots:
        robot.move(1)

    robot_positions = {r.position for r in robots}
    middle_row = max_row // 2
    upper = [r for r in robot_positions if r[0] < middle_row]
    lower = [r for r in robot_positions if r[0] > middle_row]

    if len(lower) / len(robot_positions) > 0.75:
        print(max_row * "◻️")
        print(f"-------------------{i + 1}------------------")
        print_robots()
