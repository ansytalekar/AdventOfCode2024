# Find distance between two lists of same length
# AoC Day 2 - Optimised
levels = [];

with open("LevelList.txt") as f:
    data = f.readlines();
    
    for line in data:
        levels.append([float(num) for num in line.split()]);

def check_safe(level):
    if (level[1] - level[0]) > 0:       up = True;
    else:                               up = False;

    check_arr = [x2 - x1 for x2, x1 in zip(level[1:], level[:-1])];

    if (up and not all(1 <= diff <= 3 for diff in check_arr)) or  (not up and not all(-3 <= diff <= -1 for diff in check_arr)):
        return False;
    else:
        return True;

def damper(bad_lvls):
    if any(check_safe([x for k,x in enumerate(bad_lvls) if k!=i]) for i in range(len(bad_lvls))):
        return True;
    return False;

safe_count = sum([check_safe(level) for level in levels]);
safe_count2 = sum([check_safe(level) if check_safe(level) else damper(level) for level in levels]);

print(f"Part 1: {safe_count}, Part 2: {safe_count2}");