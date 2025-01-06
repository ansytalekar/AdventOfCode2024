# Day 10 AoC
import copy;

# Recursively search down the trail
def trail_search(map, pos_dir, pos, distinct = False):

    if map[pos[0]][pos[1]] == 9:
        if distinct:
            pos_dir.append(pos);
        elif pos not in pos_dir:
            # print("Adding 9 at: ", pos)
            pos_dir.append(pos);

        return;

    look_for = map[pos[0]][pos[1]] + 1;

    directions = [[0,1], [-1,0], [1,0],[0,-1]];

    for dir in directions:
        new_pos = (pos[0]+dir[0], pos[1]+dir[1]);
    
        if (new_pos[0] >= 0 and new_pos[0] < len(map) and
            new_pos[1] >= 0 and new_pos[1] < len(map[0]) and
            map[new_pos[0]][new_pos[1]] == look_for):
                # print(look_for - 1, ": ", pos, new_pos)
                trail_search(map, pos_dir, new_pos, distinct);
        else:
            continue;

    return;

trail_grid = [];
end_pos = {};

with open("Trail.txt") as f:
    lines = f.read().splitlines()

    for i in range(len(lines)):
        trail_grid.append([]);
        str_lines = list(lines[i]);

        for j in range(len(str_lines)):
            val = int(str_lines[j])
            trail_grid[i].append(val);
        
            if val == 0:
                end_pos[(i,j)] = [];

end_pos2 = copy.deepcopy(end_pos);

for pos in end_pos.keys():
   trail_search(trail_grid, end_pos[pos], pos);

for pos in end_pos2.keys():
    trail_search(trail_grid, end_pos2[pos], pos, True);

trailheads = 0;
trailheads2 = 0;

for _, val in end_pos.items():
    trailheads += len(val);

for _, val in end_pos2.items():
    trailheads2 += len(val);


print(trailheads)
print(trailheads2)