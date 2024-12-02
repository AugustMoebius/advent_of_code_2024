
a1 = []
a2 = []

with open('input_files/day01.txt', 'r') as f:
    for line in f:
        split = line.split()
        a1.append(int(split[0]))
        a2.append(int(split[1]))


# Part 1
a1.sort()
a2.sort()

total = 0

for i in range(len(a1)):
    total += abs(a1[i] - a2[i])

print(total)

# part 2
sim_score = 0
for n1 in a1:
    count = 0
    for n2 in a2:
        if n1 == n2:
            count += 1
    sim_score += n1 * count

print(sim_score)

