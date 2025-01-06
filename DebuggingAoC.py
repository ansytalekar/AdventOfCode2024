# Day 17
import re;
from collections import defaultdict;
import time;

def dv(num1, num2):
    return int(num1 / 2**num2);

def chrono_computer(registers, command, combo, out):
    # dict, int, int, list
    combos = {0:0, 1:1, 2:2, 3:3, 4: registers["A"], 5: registers["B"], 6: registers["C"]};

    if command == 0:
        registers["A"] = dv(registers["A"], combos[combo]);
    elif command == 1:
        registers["B"] = registers["B"] ^ combo;
    elif command == 2:
        registers["B"] = combos[combo] % 8;
    elif command == 4:
        registers["B"] = registers["B"] ^ registers["C"];
    elif command == 6:
        registers["B"] = dv(registers["A"], combos[combo]);
    elif command == 7:
        registers["C"] = dv(registers["A"], combos[combo]);
    else: # if command == 5
        out.append(combos[combo] % 8);
        # print(combos[combo] % 8);

def run_program(registers, commands, out = []):
    k = 0;
    while(k < len(commands)-1):
        if commands[k] == 3:
            if registers["A"] != 0:
                k = commands[k+1];
            else:
                k += 2;
        else:
            chrono_computer(registers, commands[k], commands[k+1], out);
            k += 2;

    return out;

###################### Main ##########################
registers = defaultdict(lambda: 0);
commands = [];

with open("Debugger.txt") as f:
    data = f.read().splitlines();
    i = 0;

    while(len(data[i]) != 0):
        registers[data[i][re.search(r"(.?):", data[i]).start()]] = int("".join(re.findall(r"\d+", data[i])));
        i += 1;

    commands += [int(num) for num in re.findall("\d+", data[-1])]

sec1 = time.time();
out = run_program(registers, commands);
output = ",".join(str(num) for num in out);
print(f"Part 1: {output}, Time: {time.time()-sec1}");

#################### Part 2 ##########################
out2 = [];
sec2 = time.time();
registers["A"] = 0; registers["B"] = 0; registers["C"] = 0;
A_val = 0;

while(len(out2) <= len(commands)):
    A_val += 1;
    registers["A"] = A_val;

    out2 = run_program(registers, commands, []);
    check = [x for x,y in zip(out2, commands[-len(out2):]) if x == y];

    if len(check) == len(out2) == len(commands):
        break;
    elif len(check) == len(out2):
        A_val *= 8;

print(f"Part 2: {A_val}, Time: {time.time()-sec2}");