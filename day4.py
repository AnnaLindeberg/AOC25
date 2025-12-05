# Day 4 of Advent of Code 2024: Printing Department
# https://adventofcode.com/2024/day/4
import networkx as nx

def main():
    res1, res2 = 0, None
    G = nx.Graph()
    with open("input4.txt") as file:
        for y, row in enumerate(file):
            for x, content in enumerate(row.strip()):
                if content == '.':
                    continue
                G.add_node((x,y))

                for pos in [(x-1,y), (x-1,y-1), (x,y-1), (x+1,y-1)]:
                    if pos in G:
                        G.add_edge((x,y), pos)
    
    rolls_to_start_with = G.number_of_nodes()

    accessible_rolls = list(map(lambda t: t[0], filter(lambda d: d[1] < 4, G.degree))) # type: ignore
    res1 = len(accessible_rolls) 
    while len(accessible_rolls) > 0:
        G.remove_nodes_from(accessible_rolls)
        accessible_rolls = list(map(lambda t: t[0], filter(lambda d: d[1] < 4, G.degree))) # type: ignore

    res2 = rolls_to_start_with - G.number_of_nodes()

    print(f"Task 1: {res1}\nTask 2: {res2}")


if __name__ == '__main__':
    main()
