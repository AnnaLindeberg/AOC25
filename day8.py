# Day 8 of Advent of Code 2024: Playground
# https://adventofcode.com/2024/day/8
from collections import namedtuple
from itertools import combinations
import networkx as nx
import bisect

Point = namedtuple('Point',['x','y','z'])

def distance(pointA: Point, pointB: Point) -> float:
    return (pointA.x-pointB.x)**2 + (pointA.y-pointB.y)**2 + (pointA.z-pointB.z)**2

def DistList(points: list[Point]) -> list[tuple[float, Point, Point]]:
    res = []
    for pointA, pointB in combinations(points,2):
        D = distance(pointA, pointB)
        bisect.insort(res, (D, pointA, pointB), key=lambda t: t[0])
    return res

def solution(distances, connections, point_count):
    G = nx.Graph()
    links_added = 0
    for _, u, v in distances:
        if links_added == connections:
            three_largest = [len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)[:3]]
        
        links_added += 1
        if v not in G or u not in nx.node_connected_component(G, v):
            G.add_edge(u,v)
        if G.number_of_edges() == point_count - 1:
            res2 = u.x * v.x
            break
   
    res1 = three_largest[0]*three_largest[1]*three_largest[2]
    return res1, res2
    

def main():
    points = []
    with open("input8.txt") as file:
        for row in file:
            points.append(Point(*map(int, row.strip().split(','))))

    distances = DistList(points)
    res1, res2 = solution(distances, 1000, len(points))

    print(f"Task 1: {res1}\nTask 2: {res2}")


if __name__ == '__main__':
    main()
