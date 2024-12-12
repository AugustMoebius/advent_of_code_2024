from typing import List

numbers = []
with open('../input_files/day11.txt', 'r') as f:
    for line in f:
        numbers = [int(n) for n in line.split()]


def expand_number(number: int, blinks: int) -> dict:
    expanded = {number: 1}
    for b in range(blinks):
        print(b)
        temp = {}
        for n, amount in expanded.items():
            if n == 0:
                temp[1] = temp.get(1, 0) + amount
            elif len(str(n)) % 2 == 0:
                str_n = str(n)
                midpoint = len(str_n) // 2
                temp[int(str_n[:midpoint])] = temp.get(int(str_n[:midpoint]), 0) + amount
                temp[int(str_n[midpoint:])] = temp.get(int(str_n[midpoint:]), 0) + amount
            else:
                val = 2024 * n
                temp[val] = temp.get(val, 0) + amount

        expanded = temp

    return expanded


total = 0
for n in numbers:
    total += sum(expand_number(n, 75).values())

print(total)



