# Day 15
import numpy as np;
import re;
import os;

from difflib import Differ 


warehouse = [];
moveset = [];
robo_pos = [];

def move_bot(line):
    move = False;

    for i in range(len(line)):
        if line[i] == ".":
            line = "." + line[:i]+line[i+1:];
            move = True;
            break;
        elif line[i] == "#":
            break;

    return list(line), move;

def update_scene(scene, pos, move):
    if move == ">":
        look_in = "".join(scene[pos[0], pos[1]:]);
        line, tick = move_bot(look_in);
        scene[pos[0], pos[1]:] = line;
        new_pos = [pos[0], pos[1]+int(tick)]

    elif move == "<":
        look_in = "".join(scene[pos[0], :pos[1]+1]);
        line, tick = move_bot(look_in[::-1]);
        scene[pos[0], :pos[1]+1] = line[::-1];
        new_pos = [pos[0], pos[1]-int(tick)]
    
    elif move == "^":
        if check_up_down(scene, [pos[0] - 1, pos[1]], move):
            new_pos = [pos[0] - 1, pos[1]];
            scene[new_pos[0], new_pos[1]] = scene[pos[0], pos[1]];
            scene[pos[0], pos[1]] = ".";
        else:
            new_pos = pos;

        """ look_in = "".join(scene[:pos[0]+1, pos[1]]);
        line, tick = move_bot(look_in[::-1]);
        scene[:pos[0]+1, pos[1]] = line[::-1];
        new_pos = [pos[0]-int(tick), pos[1]]; """
    
    else:
        if check_up_down(scene, [pos[0] + 1, pos[1]], move):
            new_pos = [pos[0] + 1, pos[1]];
            scene[new_pos[0], new_pos[1]] = scene[pos[0], pos[1]];
            scene[pos[0], pos[1]] = ".";
        else:
            new_pos = pos;

        """ look_in = "".join(scene[pos[0]:, pos[1]]);
        line, tick = move_bot(look_in);
        scene[pos[0]:, pos[1]] = line;
        new_pos = [pos[0]+int(tick), pos[1]]; """

    return scene, new_pos;

def check_up_down(scene, pos, move):
    if scene[pos[0], pos[1]] == "#":
        return False;
    elif scene[pos[0], pos[1]] == ".":
        return True;
    elif scene[pos[0], pos[1]] == "[":
        if move == "^":
            if check_up_down(scene, [pos[0]-1, pos[1]], move) and check_up_down(scene, [pos[0]-1, pos[1]+1], move):
                scene[pos[0]-1, pos[1]] = "[";
                scene[pos[0]-1, pos[1]+1] = "]";
                scene[pos[0], [pos[1], pos[1]+1]] = [".", "."];
                return True;
            else:
                return False;
        else:
            if check_up_down(scene, [pos[0]+1, pos[1]], move) and check_up_down(scene, [pos[0]+1, pos[1]+1], move):
                scene[pos[0]+1, pos[1]] = "[";
                scene[pos[0]+1, pos[1]+1] = "]";
                scene[pos[0], [pos[1], pos[1]+1]] = [".", "."];
                return True;
            else:
                return False;

    elif scene[pos[0], pos[1]] == "]":
        if move == "^":
            if check_up_down(scene, [pos[0]-1, pos[1]], move) and check_up_down(scene, [pos[0]-1, pos[1]-1], move):
                scene[pos[0]-1, pos[1]] = "]";
                scene[pos[0]-1, pos[1]-1] = "[";
                scene[pos[0], [pos[1], pos[1]-1]] = [".", "."];
                return True;
            else:
                return False;
        else:
            if check_up_down(scene, [pos[0]+1, pos[1]], move) and check_up_down(scene, [pos[0]+1, pos[1]-1], move):
                scene[pos[0]+1, pos[1]] = "]";
                scene[pos[0]+1, pos[1]-1] = "[";
                scene[pos[0], [pos[1], pos[1]-1]] = [".", "."];
                return True;
            else:
                return False;

    else:
        if move == "^":
            if check_up_down(scene, [pos[0]-1, pos[1]], move):
                scene[pos[0]-1, pos[1]] = "O";
                return True;
            else:
                return False;
        else:
            if check_up_down(scene, [pos[0]+1, pos[1]], move):
                scene[pos[0]+1, pos[1]] = "O";
                return True;
            else:
                return False;


def gps(scene, part):
    sum_coords = 0;
    
    if not part:
        for i in range(len(scene)):
            for j in range(len(scene[0])):
                if scene[i,j] == "O":
                    sum_coords += 100*i + j;
    
    else:
        for i in range(len(scene)):
            """ boxes = [min([m.start(0), m.end(0) - len(scene[i])]) for m in re.finditer("\[]", "".join(scene[i]))];

            if i < len(scene) // 2:
                sum_coords += len(boxes)*100*i + sum(boxes);
            else: 
                sum_coords += len(boxes)*100*(len(scene)-i) + sum(boxes); """
            
            boxes = [min([m.start(0), m.end(0)]) for m in re.finditer("\[]", "".join(scene[i]))];
            sum_coords += len(boxes)*100*i + sum(boxes);

    return sum_coords;

########################## Main #############################
part2 = True;

# read file
with open("Lanternhouse.txt") as f:
    lines = f.read().splitlines();

    for i in range(len(lines)):
        if len(lines[i]) == 0:
            break;
        else:
            if part2: 
                to_add = "";
                
                for ltr in lines[i]:
                    if ltr == "O":
                        to_add += "[]";
                    elif ltr == "@":
                        to_add += "@.";
                    else:
                        to_add += ltr*2;
            
                if "@" in to_add: robo_pos = [i, re.search("@", to_add).start()];
                warehouse.append([ltr for ltr in to_add])
            
            else:
                if "@" in lines[i]: robo_pos = [i, re.search("@", lines[i]).start()];
                warehouse.append([ltr for ltr in lines[i]]);

    moveset = list("".join(l.rstrip() for l in lines[i:]));

# convert to np.array
scene = np.array(warehouse);

for move in moveset[0:1375]:
    scene, robo_pos = update_scene(scene, robo_pos, move);

with open("Output.txt", "w") as f: 
    for row in scene:
        print("".join(row), file = f);
    
""" os.startfile("Output.txt"); """
print(gps(scene, part2))
# quit();