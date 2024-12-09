input_data = []

with open('../input_files/day09.txt', 'r') as f:
    for line in f:
        input_data = [int(x) for x in line.strip()]


unwrapped = []
file_idx = 0
data_idx_blocks = []
free_idx_blocks = []
for idx, n in enumerate(input_data):
    insert_data = idx % 2 == 0
    if insert_data:
        data_idx_blocks.append(list(range(len(unwrapped), len(unwrapped) + n)))
        unwrapped.extend([file_idx] * n)
        file_idx += 1
    else:
        free_idx_blocks.append(list(range(len(unwrapped), len(unwrapped) + n)))
        unwrapped.extend([None] * n)




# iterate unwrapped backwards
block_idx = len(data_idx_blocks) - 1
while block_idx > 0: # Not move the first block
    print(block_idx)
    data_block = data_idx_blocks[block_idx]

    next_free_block = None
    for free_block in free_idx_blocks:
        if len(free_block) >= len(data_block) and free_block[0] < data_block[0]:
            next_free_block = free_block
            break

    if not next_free_block:
        block_idx -= 1
        continue


    for idx, data_idx in enumerate(data_block):
        unwrapped[next_free_block.pop(0)] = unwrapped[data_block[idx]]
        unwrapped[data_block[idx]] = None

    block_idx -= 1



total = 0
for idx, n in enumerate(unwrapped):
    if n is None:
        continue
    total += idx * n


print(total)