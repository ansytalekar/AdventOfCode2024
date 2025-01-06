# AoC Day 24
from functools import cache;

INPUTS = {};
CIRCUITS = {};
OPERATORS = {"AND": lambda x, y: x & y, "OR": lambda x, y: x | y, "XOR": lambda x, y: x ^ y}
SEEN = set();
COMMON = set();

@cache
def solve_circuit(circuit):
    val1, val2, func = CIRCUITS[circuit];

    if val1 in INPUTS.keys() and val2 in INPUTS.keys():
        INPUTS[circuit] = int(OPERATORS[func](INPUTS[val1], INPUTS[val2]));
    else:
        INPUTS[circuit] = int(OPERATORS[func](solve_circuit(val1), solve_circuit(val2)));

    return INPUTS[circuit];

##################### MAIN #####################
with open("LogicGate.txt") as f:
    data = f.read().splitlines();
    i = 0;

    while(len(data[i]) != 0):
        key, val = data[i].split(": ");
        INPUTS[key] = int(val);
        i += 1;

    i += 1;

    while(i < len(data)):
        vals = data[i].split(" ");
        CIRCUITS[vals[4]] = [vals[0], vals[2], vals[1]];
        i += 1;

#################### PART 1 ####################
for circuit in CIRCUITS.keys():
    solve_circuit(circuit);

bit = ["", "", ""];
INPUTS = dict(sorted(INPUTS.items()));

for key in INPUTS.keys():
    if key.startswith("x"):
        bit[0] = str(INPUTS[key]) + bit[0];
    if key.startswith("y"):
        bit[1] = str(INPUTS[key]) + bit[1];
    if key.startswith("z"):
        bit[2] = str(INPUTS[key]) + bit[2];

print(f"Part 1: {int(bit[2], 2)}");

#################### PART 2 ####################
target = bin(int(bit[0],2) + int(bit[1],2))[2:];

to_swap = [];

# Wrong bits
for i in range(len(target)):
    if target[i] != bit[2][i]:
        to_swap.append("z"+str(i).zfill(2));

bad = [];

# Finding wrong bits
""" Visually from below, other than end, z is always XOR
for key in dict(sorted(CIRCUITS.items())).keys():
    if key.startswith("z"):
        print(CIRCUITS[key][2]); """

for circuit in CIRCUITS.keys():
    val1, val2, func = CIRCUITS[circuit];

    if circuit.startswith("z") and func != "XOR":
        bad.append(circuit);
    
    if (func == "XOR" and 
    circuit[0] not in ["x", "y", "z"] and
    val1[0] not in ["x", "y", "z"] and
    val2[0] not in ["x", "y", "z"]):
        bad.append(circuit);

bad.remove("z45")
bad = bad + ["hjm", "mcq"];
print(",".join(sorted(bad)));
# from inspection, hjm and mcq are also wrong
# hjm carries the x24 AND y24 to z24 rather than z25
# mcq swaps with it to get the x24 and y24 XOR to z24


# djg,dsd,hjm,mcq,sbg,z12,z19,z37