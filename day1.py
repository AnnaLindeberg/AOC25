# Day 1 of Advent of Code 2024: Secret Entrance
# https://adventofcode.com/2024/day/1

def main():
    res1, res2 = 0, 0
    dial = 50
    with open("input1.txt") as file:
        for row in file:
            direction = row[0]
            steps = int(row[1:].strip())
            res2 += steps//100
            steps = steps % 100
            if direction == 'R':
                if dial + steps > 100:
                    res2 += 1
                dial = (dial + steps) % 100
            else:
                if dial > 0 and dial - steps < 0:
                    res2 += 1
                dial = (dial - steps) % 100
            
            if dial == 0:
                res2 += 1
                res1 += 1


    print(f"Task 1: {res1}\nTask 2: {res2}")

# 2782 too low 7015 too low

if __name__ == '__main__':
    main()
