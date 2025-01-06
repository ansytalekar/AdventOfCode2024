# AoC Day 21 - KeypadRobots

# 0,0 is the bottom right block
NUMKEY = {"A": 0+0j, "0": 1+0j, " ": 2+0j, "1": 2+1j, "2": 1+1j, "3": 0+1j, 
          "4": 2+2j, "5": 1+2j, "6": 0+2j, "7": 2+3j, "8": 1+3j, "9": 0+3j};
DIRKEY = {"A": 0+1j, "^": 1+1j, " ": 2+1j, ">": 0+0j, "v": 1+0j, "<": 2+0j};

# "Cache"
SEEN = {};

def build_sequence(start, target):
    if (start,target) in SEEN.keys():
        return SEEN[(start,target)];
    # Previously took a string input, then added keys for every string
    # Would have been too long to run, so split into two functions
    # Can do so as each key press is independently separated by A
    # Further can store calculated values into dict and avoid recalc
    # This constructs a sequence for each button pressed
    key_loc = DIRKEY if (target in DIRKEY.keys() and start in DIRKEY.keys()) else NUMKEY;

    dist = (key_loc[target] - key_loc[start]);
    lr, ud = int(dist.real), int(dist.imag)
    vert = "^"*ud + "v"*-ud;
    horz = "<"*lr + ">"*-lr;

    open = key_loc[" "] - key_loc[start];
    vh_pref = (lr < 0 or open.real == lr) and open != ud*1j;
    # Logic for above: Robot CANNOT see any blank spaces
    # First condition: If going right, vertical is preferred
    # Second condition: When going left, prevents <v into the blank
    # Third condition: The y-change is different from the blank - 
    #   > to ^ would be False, since the change is 1j

    SEEN[(start,target)] = (vert+horz if vh_pref else horz+vert) + "A"; 
    return  SEEN[(start,target)];

# Recur down for each character till desired output
def comm_length(code, level):
    if (code, level) in SEEN.keys():
        return SEEN[(code, level)];

    if level == 0:
        SEEN[(code,level)] = len(code);
        return len(code);

    SEEN[(code,level)] = 0;
    for pos, ltr in enumerate(code):
        SEEN[(code,level)] += comm_length(build_sequence(code[pos-1], ltr), level - 1);
        
    return SEEN[(code,level)];

###################### MAIN ######################
codes = open("KeypadCodes.txt").read().splitlines();

################### PART 1 & 2 ###################
complexity = [0,0];
for code in codes:
    complexity[0] += int(code[:3])*comm_length(code, 3);
    complexity[1] += int(code[:3])*comm_length(code, 26);

print(f"Part 1: {complexity[0]}, Part 2: {complexity[1]}");