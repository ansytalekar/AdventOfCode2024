# AoC Day 20 - Pico Races
import re;
import heapq;
import time;

DIRS = [(0,1), (-1,0), (0,-1), (1,0)];

####################### FUNCS #######################
# Check dictionary
def check_dict_dist(target_dict, key, val):
    ''' Check for Dijkstra if position in dictionary and new distance is smaller than old '''
    if key in target_dict.keys() and val > target_dict[key]:    return True;
    else: return False;

def in_grid(grid, loc):
    ''' Checks that the location loc is within grid bounds '''
    if (loc[0] >= 0 and loc[0] < len(grid) and
        loc[1] >= 0 and loc[1] < len(grid[0])):
        return True;
    return False;

# Dijkstra - Route Minimisation Function
def dijkstra(maze, start, end, lowest, loc_dir = {}):
    queue = [];
    heapq.heappush(queue, (0, start, (0,1))); # distance, position, direction

    while queue:
        dist, current, curr_dir = heapq.heappop(queue);
        
        if current == end and dist <= lowest:
            lowest = dist;

        # for some reason this only works if check_dict_dist is modified [likely due to same weightage for any branch]
        if check_dict_dist(loc_dir, current, dist): continue;
        else: loc_dir[current] = dist;
        
        next_dirs = [curr_dir, DIRS[(DIRS.index(curr_dir)+1)%4], DIRS[(DIRS.index(curr_dir)+3)%4]];

        for heading in next_dirs:
            next_pos = (current[0]+heading[0], current[1]+heading[1]);
                    
            if in_grid(maze, next_pos) and maze[next_pos[0]][next_pos[1]] != "#":
                heapq.heappush(queue, (dist+1, next_pos, heading));

    return lowest;

def circular_range(maze, pos, limit):
    arr = {};

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if abs(i-pos[0]) + abs(j-pos[1]) <= limit and maze[i][j] != "#":
                arr[(i,j)] = abs(i-pos[0]) + abs(j-pos[1]);

    return arr;

###################### MAIN ######################
maze = [];
loc_dist = {};

with open("PicoMap.txt") as f:
    lines = f.read().splitlines()
    
    for i in range(len(lines)):
        maze.append([ltr for ltr in lines[i]]);
        if "S" in lines[i]: start_pos = (i, re.search("S", lines[i]).start());
        if "E" in lines[i]: end_pos = (i, re.search("E", lines[i]).start());

loc_dist[start_pos] = dijkstra(maze, end_pos, start_pos, 10**8, loc_dist);

#################### PART 1 & 2 ####################
count = [0, 0];         # Part 1, Part 2
sec1 = time.time();

for loc in loc_dist:
    cheats = [2, 20];

    for i in range(len(cheats)):
        search_in = circular_range(maze, loc, cheats[i]);

        for search in search_in.keys():
            if search in loc_dist.keys() and (loc_dist[loc] - loc_dist[search] - search_in[search]) >= 100:
                count[i] += 1;

print(f"Part 1: {count[0]}, 2: {count[1]}, Time: {round(time.time() - sec1, 4)}s");