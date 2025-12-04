# Day 3 of Advent of Code 2024: Lobby
# https://adventofcode.com/2024/day/3

def dropOne(s):
    # s= abcde -> [bcde, acde, abde, abce, abcd]
    res = []
    for i in range(len(s)):
        res.append(s[:i]+s[i+1:])
    return res

def best_joltage(banks, digits):
    joltage = int(banks[:digits])
    for d in banks[digits:]:
        candidates = [joltage] + [int(c + d) for c in dropOne(str(joltage))]
        joltage = max(candidates)
    return joltage


def main():
    res1, res2 = 0, 0
    with open("input3.txt") as file:
        for row in file:
            banks = row.strip()
            res1 += best_joltage(banks, 2)
            res2 += best_joltage(banks, 12)


    print(f"Task 1: {res1}\nTask 2: {res2}")


if __name__ == '__main__':
    main()
