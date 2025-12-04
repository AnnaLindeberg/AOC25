# Day 2 of Advent of Code 2024: Gift Shop
# https://adventofcode.com/2024/day/2

def inRanges(ranges, x):
    for left, right in ranges:
        if left <= x <= right:
            return True
    return False

def main():
    res1, res2 = set(), set()
    with open("input2.txt") as file:
        for row in file:
            ranges = list(map(lambda P: tuple(map(int, P.split('-'))), row.strip().split(',')))

    ranges.sort()
    maxi = str(ranges[-1][-1])
    maxprefix = int(maxi[:len(maxi)//2])
    for pattern in range(1, maxprefix + 1):
        repeats = 2
        while len(str(pattern))*repeats <= len(maxi):
            ID = int(str(pattern)*repeats)
            if inRanges(ranges, ID):
                if repeats == 2:
                    res1.add(ID)
                res2.add(ID)
            repeats += 1
        
    res1, res2 = sum(res1), sum(res2)
    print(f"Task 1: {res1}\nTask 2: {res2}")



if __name__ == '__main__':
    main()