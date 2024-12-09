input_data = []

with open('../input_files/day09.txt', 'r') as f:
    for line in f:
        input_data = [int(x) for x in line.strip()]


unwrapped = []
file_idx = 0

for idx, n in enumerate(input_data):
    insert_data = idx % 2 == 0
    if insert_data:
        unwrapped.extend([file_idx] * n)
        file_idx += 1
    else:
        unwrapped.extend([None] * n)




def find_next_free_idx(unwrapped, start_idx):
    for idx, val in enumerate(unwrapped[start_idx:]):
        if val is None:
            return start_idx + idx
    return None



next_free_idx = 0
# iterate unwrapped backwards
idx = len(unwrapped) - 1
while idx >= 0:
    to_move = unwrapped[idx]
    if not to_move:
        idx -= 1
        continue
    next_free_idx = find_next_free_idx(unwrapped, next_free_idx)
    if next_free_idx > idx:
        break
    unwrapped[next_free_idx] = to_move
    unwrapped[idx] = None
    idx -= 1


total = 0

for idx, n in enumerate(unwrapped):
    if n is None:
        break
    total += idx * n


print(total)