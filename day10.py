# Day 10 of Advent of Code 2024: Factory
# https://adventofcode.com/2024/day/10
from collections import namedtuple, deque
import networkx as nx
import matplotlib.pyplot as plt
from scipy.optimize import LinearConstraint
from scipy.optimize import milp
import numpy as np


MachineConfig = namedtuple('MachineConfig', ['light', 'buttons', 'joltages'])

def parseRow(row):
    S =  "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"
    rightSbracket = row.index(']')
    leftCbracket = row.index('{')
    light_diagram = tuple(0 if c == '.' else 1 for c in row[1:rightSbracket] )
    joltages = tuple(map(int, row[leftCbracket+1:-1].split(',')))
    buttons = row[rightSbracket+3:leftCbracket-2]
    buttons = list(map(lambda seq: tuple(map(int, seq.split(','))), buttons.split(') (')))
    return MachineConfig(light_diagram, buttons, joltages)

def sol1(config: MachineConfig):
    start = tuple(0 for _ in config.light)
    lightCount = len(start)
    M = nx.DiGraph()
    M.add_node(start)
    queue = deque([start])
    while queue:
        state = queue.popleft()
        if state == config.light:
            break
        
        for button in config.buttons:
            newState = tuple((state[i] + (i in button))% 2 for i in range(lightCount))
            if newState not in M:
                M.add_edge(state, newState)
                queue.append(newState)
    clicks = nx.shortest_path_length(M, source=tuple(0 for _ in config.light), 
                                                target=config.light)
    return clicks

def sol2(config: MachineConfig):
    # minimize c*x where
    # min_cliques ≤ Ax ≤ max_cliques
    c = np.ones(len(config.buttons))
    A = []
    for button in config.buttons:
        row = [1 if i in button else 0 for i in range(len(config.light))]
        A.append(row)
    A = np.array(A).transpose()


    max_clicks = np.array(config.joltages, dtype=float)
    min_clicks = max_clicks.copy()
    constraints = LinearConstraint(A, min_clicks, max_clicks) # type: ignore
    
    # every coord of x should be integer
    integrality = np.ones_like(c)
    
    res = milp(c=c, constraints=constraints, integrality=integrality)
    
    return int(sum(res.x))


def main():
    res1, res2 = 0, 0
    with open("input10.txt") as file:
        for row in file:
            config = parseRow(row.strip())
            res1 += sol1(config)
            res2 += sol2(config)
            
    print(f"Task 1: {res1}\nTask 2: {res2}")


if __name__ == '__main__':
    main()
