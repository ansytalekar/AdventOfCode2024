# AoC Day 19
import time

PATTERNS = [];
SEEN = {"": 1};   # <- in place of cache

###################################### FUNC ######################################
def pop_pattern(designs):
    if designs in SEEN.keys():
        return SEEN[designs];
    else:
        val = sum(pop_pattern(designs[len(pattern):]) for pattern in PATTERNS if designs.startswith(pattern));
        SEEN[designs] = val;
        return val; 

###################################### MAIN ######################################
with open("Towels.txt") as f:
    P, _, *designs = f.read().splitlines();
    PATTERNS = P.split(", ");                       # populate patterns

count = [];
sec1 = time.time();

for design in designs:                              # design in designs:
    count.append(pop_pattern(design));

print("Part 1:", len([num for num in count if num != 0]), "Part 2:", sum(count), "Time:", time.time() - sec1);