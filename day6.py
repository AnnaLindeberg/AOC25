# Day 6 of Advent of Code 2024: Trash Compactor
# https://adventofcode.com/2024/day/6
from functools import reduce  # Required in Python 3
import operator

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

def sol1(rows):
    res = 0
    for problem in zip(*rows):
        if problem[-1] == '+':
            res += sum(map(int, problem[:-1]))
        else:
            res += prod(map(int, problem[:-1]))
    return res

def sol2(rows):
    no_row, no_col = len(rows), len(rows[0])
    numbers = []
    cidx = no_col - 1
    res = 0
    while cidx >= 0:
        num = "".join([rows[ridx][cidx] for ridx in range(no_row - 1)])
        numbers.append(int(num))
        if rows[no_row-1][cidx] == '+':
            res += sum(numbers)
            cidx -= 2
            numbers = []
        elif rows[no_row-1][cidx] == '*':
            res += prod(numbers)
            cidx -= 2
            numbers = []
        else:
            cidx -= 1
    
    return res



def main():
    res1, res2 = 0, None
    rows = []
    with open("input6.txt") as file:
        for row in file:
            rows.append(row[:-1])

    res1 = sol1([r.split() for r in rows])
    res2 = sol2(rows)

    print(f"Task 1: {res1}\nTask 2: {res2}")


if __name__ == '__main__':
    main()
