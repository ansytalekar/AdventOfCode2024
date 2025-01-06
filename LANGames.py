# AoC Day 23 - LAN Games
import networkx as nx;

CONNECT = {};
LAN3 = set();
PATH = [];
MIN = [2];

####################### FUNC #######################
def dfs(node, depth, change_min = False):
    if depth == 0:
        return;

    PATH.append(node)

    neighbours = CONNECT[node];

    for neighbour in neighbours:
        if neighbour in PATH:
            # In cycle
            start = PATH.index(neighbour)
            cycle = tuple(sorted(PATH[start:]));
    
            if len(cycle) > MIN[-1] and cycle not in LAN3:
                LAN3.add(cycle);
                if change_min: MIN.append(len(cycle));

        else:
            dfs(neighbour, depth - 1, change_min);
    
    PATH.pop()

def add_to_dict(target_dict, key, val):
    if key in target_dict.keys():
        target_dict[key].append(val);
    else:
        target_dict[key] = [val];

####################### MAIN #######################
data = open("LANNetwork.txt").read().splitlines();
for line in data:
    node1, node2 = line.split("-");
    add_to_dict(CONNECT, node1, node2);
    add_to_dict(CONNECT, node2, node1);

for node in CONNECT.keys():
    PATH = [];
    dfs(node, 3);

count = 0;
for cycle in LAN3:
    if any(node.startswith("t") for node in cycle):
        count += 1;

print(f"Part 1: {count}");

###################### PART 2 ######################
G = nx.Graph();
G.add_edges_from((node1, node2) for node1, node2 in [line.split("-") for line in data]);
longest = nx.approximation.max_clique(G);
print(",".join(sorted(longest)));