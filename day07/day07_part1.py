import itertools

equations = {}

with open('../input_files/day07.txt', 'r') as f:
    for line in f:
        split = line.split(":")
        equations[int(split[0])] = [int(n) for n in split[1].split()]

print()

def generate_combinations(n):
    return [list(combo) for combo in itertools.product([0, 1], repeat=n)]

total = 0
for k, v in equations.items():
    combinations = generate_combinations(len(v)-1)

    for comb in combinations:
        result = v[0]
        for i in range(1, len(v)):
            operator = comb.pop()
            if operator == 0:
                result += v[i]
            else:
                result *= v[i]

        if result == k:
            total += result
            break

print(total)


