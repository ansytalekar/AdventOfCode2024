# AoC Day 19
import time

PATTERNS = [];
SEEN = {"": 1};

###################################### FUNC ######################################
def check_design(design):
    if design in SEEN.keys():
        return SEEN[design];
    else:
        val = sum( all([check_design(sections) for sections in design.split(pattern)]) for pattern in PATTERNS if pattern in design );
        SEEN[design] = val;
        return val;

###################################### MAIN ######################################
with open("Towels.txt") as f:
    P, _, *designs = f.read().splitlines();
    PATTERNS += P.split(", ");                      # adding patterns

sec1 = time.time()
count = [];

for design in designs:                              # design in designs:
    count.append(check_design(design));

print("Part 1:", len([num for num in count if num != 0]), "Part 2:", sum(count), "Time:", time.time() - sec1);