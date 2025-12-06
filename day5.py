# Day 5 of Advent of Code 2024: Cafeteria
# https://adventofcode.com/2024/day/5
from itertools import pairwise

def mergeRanges(ranges):
    newRanges = []
    idxA, idxB = 0, 1
    rangeA = ranges[idxA]
    while idxA < len(ranges):
        if idxB >= len(ranges):
            newRanges.append(rangeA)
            idxA = idxB
            continue
        rangeB = ranges[idxB]
        if rangeA[1] < rangeB[0]:
            newRanges.append(rangeA)
            idxA = idxB
            rangeA = rangeB
            idxB += 1
        elif rangeA[1] <= rangeB[1]:
            rangeA = [rangeA[0], rangeB[1]]
            idxB += 1
        else:
            idxB += 1
    return newRanges



def inRanges(ranges, x):
    for left, right in ranges:
        if left <= x <= right:
            return True
    return False

def main():
    res1, res2 = 0, None
    readingRanges = True
    ranges = []
    produce = []
    with open("input5.txt") as file:
        for row in file:
            if row.strip() == "":
                readingRanges = False
                ranges.sort()
                continue
            if readingRanges:
                num_range = list(map(int, row.strip().split('-')))
                ranges.append(num_range)
            else:
                produce.append(int(row.strip()))


    ranges = mergeRanges(ranges)
    res1 = sum(1 for _ in filter(lambda p: inRanges(ranges, p), produce))
    res2 = sum(map(lambda t: t[1]-t[0]+1, ranges))

    print(f"Task 1: {res1}\nTask 2: {res2}")


if __name__ == '__main__':
    main()
