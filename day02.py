reports = []


with open('input_files/day02.txt', 'r') as f:
    for line in f:
        reports.append([int(n) for n in line.split()])




def report_valid(report: list[int]) -> bool:
    order_func = (lambda n1, n2: n1 < n2) if report[0] < report[1] else (lambda n1, n2: n1 > n2)
    for i in range(len(report) - 1):
        n1 = report[i]
        n2 = report[i + 1]
        if not order_func(n1, n2):
            return False
        if abs(n1 - n2) > 3:
            return False
    return True



def part1():
    safe_count = 0
    for report in reports:
        if report_valid(report):
            safe_count += 1
    return safe_count

print(part1())


# Part 2
def part_2():
    safe_count = 0
    for report in reports:
        if report_valid(report):
            safe_count += 1
            continue

        for i in range(len(report)):
            r_copy = report.copy()
            r_copy.pop(i)
            if report_valid(r_copy):
                safe_count += 1
                break
    return safe_count



print(part_2())