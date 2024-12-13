import re

machines = []


class Machine:
    def __init__(self):
        self.a_offset = None
        self.b_offset = None
        self.prize = None

    def __repr__(self):
        return f"Machine(a_offset={self.a_offset}, b_offset={self.b_offset}, prize={self.prize})"


with open('../input_files/day13.txt', 'r') as f:
    machine = Machine()
    pattern = re.compile(r'(\d+)')
    for line in f:
        matches = pattern.findall(line)
        if line.startswith("Button A:"):
            machine.a_offset = (int(matches[0]), int(matches[1]))
            continue
        if line.startswith("Button B:"):
            machine.b_offset = (int(matches[0]), int(matches[1]))
            continue
        if line.startswith("Prize:"):
            machine.prize = (int(matches[0]), int(matches[1]))
            machines.append(machine)
            continue
        machine = Machine()


def find_best_price(m: Machine) -> int:
    prices = []
    for a in range(100):
        for b in range(100):
            x = a * m.a_offset[0] + b * m.b_offset[0]
            y = a * m.a_offset[1] + b * m.b_offset[1]
            if (x, y) == m.prize:
                prices.append(3 * a + b)

    if len(prices) == 0:
        return 0

    return min(prices)


total = 0

for mach in machines:
    total += find_best_price(mach)

print(total)
