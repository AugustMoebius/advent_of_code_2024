from typing import List

rules = {}
updates = []

with open('../input_files/day05.txt', 'r') as f:
    read_rules = True
    lines = f.readlines()
    while len(lines) > 0:
        line = lines.pop(0)
        if line == "\n":
            read_rules = False
            continue
        if read_rules:
            split = line.split("|")
            rules.setdefault(int(split[0]), []).append(int(split[1]))
        else:
            updates.append([int(n) for n in line.split(",")])




def validate_update(update: List[int]) -> int:
    for idx, n in enumerate(update):
        n_rules = rules.get(n, [])
        before_slice = update[0:idx]
        intersection = list(set(n_rules) & set(before_slice))
        if len(intersection) > 0:
            return 0

    return update[int((len(update) - 1)/2)]


total = 0

invalid_updates = []

for update in updates:
    valid_count = validate_update(update)
    if valid_count == 0:
        invalid_updates.append(update)
    total += valid_count

# Part 1
print(total)


# Part 2


def fix_update(invalid_update: List[int]) -> int:
    fixed_update = invalid_update.copy()
    while True:
        for idx, n in enumerate(fixed_update):
            n_rules = rules.get(n, [])
            before_slice = fixed_update[0:idx]
            intersection = list(set(n_rules) & set(before_slice))
            for error in intersection:
                fixed_update.remove(error)
                fixed_update.insert(idx, error)
        valid_count = validate_update(fixed_update)
        if valid_count != 0:
            return valid_count


total_2 = 0

for i_update in invalid_updates:
    total_2 += fix_update(i_update)

print(total_2)


