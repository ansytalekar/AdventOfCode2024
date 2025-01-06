# Find distance between two lists of same length
levels = [];

with open("LevelList2.txt") as f:
    data = f.readlines();

    for line in data:
        l = line.split();
        levels.append([float(i) for i in l])

safe_count = 0;

def check_safe(level):
    up = False;

    if (level[1] - level[0]) > 0:
        up = True;

    for i in range(len(level) - 1):
        if up and not ((level[i+1]-level[i]) >= 1 and (level[i+1]-level[i]) <= 3):
            return 0;
        elif not up and not ((level[i+1]-level[i]) <= -1 and (level[i+1]-level[i]) >= -3):
            return 0;
        else: 
            pass;

    return 1;

def damper(bad_lvls):
    for i in range(len(bad_lvls)):
        if check_safe([x for k,x in enumerate(bad_lvls) if k!=i]):
            return True;
        else:
            continue;

    return False;

for level in levels:
    counter = check_safe(level);
    
    if counter == 1:
        safe_count += check_safe(level);
    
    else:
        if damper(level):
            safe_count += 1;
        else: 
            pass;
    pass; 


print(safe_count);