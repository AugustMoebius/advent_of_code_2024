import re

command = ""

with open('input_files/day03.txt', 'r') as f:
    for line in f:
        command += line

def part1():
    pattern = r"mul\((\d+),(\d+)\)"

    # Find all matches
    matches = re.findall(pattern, command)

    # Extracted groups
    extracted_groups = [int(m[0]) * int(m[1]) for m in matches]
    print(sum(extracted_groups))


def part2():
    pattern = r"(don't\(\)|do\(\))?(?:mul\((\d+),(\d+)\))?"
    matches = re.findall(pattern, command)
    total = 0
    enabled = True

    # remove empty matches
    matches = [m for m in matches if m[0] != "" or m[1] != ""]

    while len(matches) > 0:
        match = matches.pop(0)
        if match[0] == "do()":
            enabled = True
        elif match[0] == "don't()":
            enabled = False

        # Check if match contains numeric chars
        if enabled and match[1] != "":
            print(f"{match}<-")
            total += int(match[1]) * int(match[2])
        else:
            print(f"{match}")

    print(total)

part1()
part2()

