# Day 11 of Advent of Code 2024: Reactor
# https://adventofcode.com/2024/day/11
import networkx as nx

def pathCount(graph: nx.DiGraph, source, target):
    try:
        nx.shortest_path(graph, source, target)
    except Exception:
        return 0
    path_counts = {target: 1}
    while source not in path_counts:
        for v in graph:
            if v not in path_counts and all(u in path_counts for _, u in graph.out_edges(v)):
                path_counts[v] = sum(path_counts[u] for _, u in graph.out_edges(v))
    return path_counts[source]


def sol2(graph):
    svr_dac = pathCount(graph, 'svr', 'dac')
    dac_fft = pathCount(graph, 'dac', 'fft')
    fft_out = pathCount(graph, 'fft', 'out')
    svr_fft = pathCount(graph, 'svr', 'fft')
    fft_dac = pathCount(graph, 'fft', 'dac')
    dac_out = pathCount(graph, 'dac', 'out')
    return svr_dac*dac_fft*fft_out + svr_fft*fft_dac*dac_out

def main():
    res1, res2 = None, None
    G = nx.DiGraph()
    with open("input11.txt") as file:
        for row in file:
            v = row[:3]
            for u in row.strip()[5:].split():
                G.add_edge(v,u)
    
    res1 = pathCount(G, 'you', 'out')
    res2 = sol2(G)

    print(f"Task 1: {res1}\nTask 2: {res2}")


if __name__ == '__main__':
    main()
