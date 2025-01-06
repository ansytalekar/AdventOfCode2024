import re
import numpy as np
import scipy.linalg as linalg

def isinteger(x):
    return np.equal(np.mod(x, 1), 0)

machines = [];

with open("Arcade.txt") as f:
    lines = f.readlines();

    for i in range(0, len(lines), 4):
        a = re.findall(r'\+\d+', lines[i]);
        b = re.findall(r'\+\d+', lines[i+1]);
        prize = re.findall(r'\d+', lines[i+2]);

        a = [int(i) for i in a]
        b = [int(i) for i in b]
        prize = [10000000000000+int(i) for i in prize];

        machines.append([a,b,prize]);

total = 0;
token_cost = [3,1];

for machine in machines: 
    add = True;

    left_matrix = np.array(machine[:-1]);
    left_matrix_T = left_matrix.T;

    solve_for = np.array(machine[-1]);

    lu = linalg.lu_factor(left_matrix_T);

    x = linalg.lu_solve(lu, solve_for);

    for sol in x:
        if abs(np.round(sol) - sol) >= 0.01:
            add = False;
    
    if add:
        total += sum([x[i]*token_cost[i] for i in range(len(x))]);

print(total)