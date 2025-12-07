# Day 7 of Advent of Code 2024: Laboratories
# https://adventofcode.com/2024/day/7
from itertools import pairwise

def sol1(diagram):
    splits = 0
    beams = set([diagram[0].index('S')])
    diagram = diagram[1:]
    for row in diagram:
        newBeams = set()
        for i, symb in enumerate(row):
            if symb == '.' and i in beams:
                newBeams.add(i)
            elif symb == '^' and i in beams:
                newBeams.add(i-1)
                newBeams.add(i+1)
                splits += 1
        beams = newBeams
    
    return  splits


def sol2(diagram):
    width = len(diagram[0])
    paths_below = [1 for _ in range(width)]
    for lower, higher in pairwise(diagram[::-1]):
        new_paths = []
        i = 0
        for lsymb, hsymb in zip(lower, higher):
            if hsymb == 'S':
                return paths_below[i]
            elif (lsymb, hsymb) == ('.', '.'):
                new_paths.append(paths_below[i])
            elif (lsymb, hsymb) == ('^', '.'):
                new_paths.append(paths_below[i-1]+paths_below[i+1])
            elif (lsymb, hsymb) == ('.', '^'):
                new_paths.append(0)
            else:
                print('what')
            i += 1
        paths_below = new_paths
            



def main():
    res1, res2 = None, None
    diagram = []
    with open("input7.txt") as file:
        for row in file:
            diagram.append(row.strip())
    
    res1 = sol1(diagram)
    res2 = sol2(diagram)
        

    print(f"Task 1: {res1}\nTask 2: {res2}")


if __name__ == '__main__':
    main()
