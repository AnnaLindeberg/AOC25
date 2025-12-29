# Day 12 of Advent of Code 2024: Christmas Tree Farm
# https://adventofcode.com/2024/day/12

def parse_tree_row(row: str) -> tuple[tuple[int, ...], tuple[int, ...]]:
    size, presents = row.strip().split(': ')
    size = tuple(map(int, size.split('x')))
    presents = tuple(map(int, presents.split()))
    return size, presents

def stupidly_fits(size, presents):
    width, height = size
    presents = sum(presents)
    return presents <= (width//3)*(height//3)

def main():
    res1, res2 = None, None
    with open("input12.txt") as file:
        lines = file.readlines()
        shapes, trees = lines[:30], lines[30:]
        trees = list(map(parse_tree_row, trees))
    
    res1 = sum(map(lambda x: stupidly_fits(*x), trees)) # type: ignore

    print(f"Task 1: {res1}\nTask 2: {res2}")


if __name__ == '__main__':
    main()
