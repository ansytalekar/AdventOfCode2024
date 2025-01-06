# Day 15
import numpy as np;
import re;
import time;

DIR = {"v": [1,0], "^": [-1,0], ">": [0,1], "<": [0,-1]};
ltr_append = {"@": "@.", "O": "[]", ".": "..", "#":"##"};

##################### Functions ##########################
def check_scene(scene, dir_key, pos):
    move = DIR[dir_key];
    x,y = [pos[0]+move[0], pos[1]+move[1]];

    if scene[x,y] == "#":
        return False;
    elif scene[x,y] == ".":
        return True;
    elif scene[x,y] == "[" and (dir_key == "^" or dir_key == "v"):
        return check_scene(scene, dir_key, [x,y]) and check_scene(scene, dir_key, [x,y+1]);
    elif scene[x,y] == "]" and (dir_key == "^" or dir_key == "v"):
        return check_scene(scene, dir_key, [x,y]) and check_scene(scene, dir_key, [x,y-1]);
    else:
        return check_scene(scene, dir_key, [x,y]);

def update_scene(scene, dir_key, pos):
    move = DIR[dir_key];
    x,y = [pos[0]+move[0], pos[1]+move[1]];

    if scene[x][y] == ".":
        scene[x][y] = scene[pos[0]][pos[1]];
        scene[pos[0]][pos[1]] = ".";
    
    elif scene[x,y] == "[" and (dir_key == "^" or dir_key == "v"):
        update_scene(scene, dir_key, [x,y]);
        update_scene(scene, dir_key, [x,y+1]);
        scene[x][y] = scene[pos[0]][pos[1]];
        scene[pos[0]][pos[1]] = ".";

    elif scene[x,y] == "]" and (dir_key == "^" or dir_key == "v"):
        update_scene(scene, dir_key, [x,y]);
        update_scene(scene, dir_key, [x,y-1]);
        scene[x][y] = scene[pos[0]][pos[1]];
        scene[pos[0]][pos[1]] = ".";
    
    else:
        update_scene(scene, dir_key, [x,y]);
        scene[x][y] = scene[pos[0]][pos[1]];
        scene[pos[0]][pos[1]] = ".";

def gps(scene, part2 = False):
    sum_coords = 0;

    for i in range(len(scene)):
        if not part2:
            boxes = [m.start() for m in re.finditer("O", "".join(scene[i]))];

        else:
            boxes = [m.start() for m in re.finditer("\[]", "".join(scene[i]))];
    
        sum_coords += len(boxes)*100*i + sum(boxes);
    
    return sum_coords;

####################### Main #############################
part2 = True;

warehouse = [];
# additional holders, robo_pos for robot starting position, moveset for all moves

# read file
with open("Lanternhouse.txt") as f:
    lines = f.read().splitlines();
    i = 0;

    while(len(lines[i]) != 0):
        if part2:
            to_add = "".join([ltr_append[ltr] for ltr in lines[i]]);
            if "@" in to_add: robo_pos = [i, re.search("@", to_add).start()];
            warehouse.append([ltr for ltr in to_add])
        else:
            if "@" in lines[i]: robo_pos = [i, re.search("@", lines[i]).start()];
            warehouse.append([ltr for ltr in lines[i]]);

        i += 1;

    moveset = list("".join(l.rstrip() for l in lines[i:]));

# convert to np.array
scene = np.array(warehouse);
sec = time.time();

for move in moveset:
    if check_scene(scene, move, robo_pos):
        update_scene(scene, move, robo_pos);
        robo_pos = [robo_pos[0] + DIR[move][0], robo_pos[1] + DIR[move][1]];

print(gps(scene, part2))
out_str = "Part 2:" if part2 else "Part 1: ";
print(f"{out_str} {time.time() - sec} s ");