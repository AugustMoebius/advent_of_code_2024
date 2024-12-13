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
            machine.prize = (10000000000000 + int(matches[0]), 10000000000000 + int(matches[1]))
            machines.append(machine)
            continue
        machine = Machine()


def find_solutions(X, Y, x_A, x_B, y_A, y_B):
    solutions = []

    # Coefficients for the linear combination
    numerator = Y * x_A - X * y_A
    denominator = y_B * x_A - x_B * y_A

    # Check if the denominator is zero to avoid division by zero
    if denominator == 0:
        return 0  # No solutions possible

    # Check if the result is an integer
    if numerator % denominator == 0:
        n_B = numerator // denominator
        # Calculate n_A
        if (X - n_B * x_B) % x_A == 0:
            n_A = (X - n_B * x_B) // x_A

            solutions.append(3* n_A + n_B)


    if len(solutions) == 0:
        return 0

    return min(solutions)

total = 0

for mach in machines:
    print(mach)
    total += find_solutions(mach.prize[0], mach.prize[1], mach.a_offset[0], mach.b_offset[0], mach.a_offset[1], mach.b_offset[1])

print(total)
