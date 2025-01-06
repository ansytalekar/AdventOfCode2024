# AoC Day 12
import copy;

def in_grid(grid, loc):
    ''' Checks that the location loc is within grid bounds '''

    if (loc[0] >= 0 and loc[0] < len(grid) and
        loc[1] >= 0 and loc[1] < len(grid[0])):

        return True;

    return False;

def plot_loc(garden, plot_dir, pos):
    ''' Recursively looks for plots and determines values '''
    # value being searched
    search = garden[pos[0]][pos[1]]

    # exit recursive tree if position previously found
    if pos in plot_dir[search]["Plot_Locs"].keys():
        return;

    # otherwise add position to investigated plots
    else:
        plot_dir[search]["Plot_Locs"][pos] = [];
        plot_dir[search]["Perimeter"] += 4;
        plot_dir[search]["Area"] += 1;       

    # directions to look in, by default each side has a wall
    directions = [(0,1), (-1,0), (0,-1),(1,0)];
    walls = [(0,1), (-1,0), (1,0),(0,-1)];
    check_dir = [];

    # Recursively step to next plot, removes walls if next step exists
    # Add a direction check for future side calculations
    for dir in directions:
        new_pos = (pos[0]+dir[0], pos[1]+dir[1]);
    
        if (in_grid(garden, new_pos) and garden[new_pos[0]][new_pos[1]] == search):
                walls.remove(dir);
                check_dir.append(dir);
                
                plot_dir[search]["Perimeter"] -= 1;
                plot_loc(garden, plot_dir, new_pos)
        else:
            continue;
    
    # Side checking
    check_walls = set(walls);

    # Checks along open paths within a plot
    for dir in check_dir:
        # Checking in a cross away from the current position
        check_pos = copy.copy(pos);
        new_wall = [];

        # looping until the grid is left, can't find the current plot (search) or \
        # a previously unsearched position is reached
        while(True):
            check_pos = (check_pos[0]+dir[0], check_pos[1]+dir[1]);

            if not (in_grid(garden, check_pos) and garden[check_pos[0]][check_pos[1]] == search
                    and check_pos in plots[region]["Plot_Locs"].keys()):
                break;
            
            # checks around for any branches that would indicate end of a side
            for surr in check_walls:
                cross_check = (check_pos[0]+surr[0], check_pos[1]+surr[1]);

                if (in_grid(garden, cross_check) and garden[cross_check[0]][cross_check[1]] == search):
                    new_wall.append(surr);

            # removes any walls already accounted for
            cur_pos_walls = plot_dir[search]["Plot_Locs"][check_pos];
            check_walls = set([wall for wall in check_walls if wall not in cur_pos_walls]);

        # readds walls that were removed AFTER a branch was found, so wall still counts as a side
        check_walls.update(new_wall);
    
    # adds the number of new walls for each position
    # stores the wall for a given position
    plot_dir[search]["Sides"] += len(check_walls);
    plot_dir[search]["Plot_Locs"][pos] = walls;

################### Main #########################
garden = [];
plots = {};

with open("Garden.txt") as f:
    lines = f.read().splitlines()

    for i in range(len(lines)):
        garden.append([]);
        str_lines = list(lines[i]);

        for j in range(len(str_lines)):
            val = str_lines[j]
            garden[i].append(val);

            if val not in plots.keys():
                plots[val] = {"Perimeter": 0, "Area": 0, "Sides": 0, "Plot_Locs": {}};

cost = 0;
cost2 = 0;

for i in range(len(garden)):
    for j in range(len(garden[0])):
        region = garden[i][j]

        if (i,j) not in plots[region]["Plot_Locs"].keys():
            cost += plots[region]["Perimeter"] * plots[region]["Area"];
            cost2 += plots[region]["Sides"] * plots[region]["Area"];

            plots[region]["Perimeter"] = 0;
            plots[region]["Area"] = 0;
            plots[region]["Sides"] = 0;
            plot_loc(garden, plots, (i,j));
            print(region, plots[region]["Area"], plots[region]["Sides"])

for key in plots.keys():
    cost += plots[key]["Perimeter"] * plots[key]["Area"]
    cost2 += plots[key]["Sides"] * plots[key]["Area"];

print(f"Without Discount = {cost}")
print(f"With Discount = {cost2}")