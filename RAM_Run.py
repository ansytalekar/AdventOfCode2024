# AoC Day 18
import heapq;
import time;

DIRS = [(0,1), (-1,0), (0,-1), (1,0)];

# Check dictionary
def check_dict_dist(target_dict, key, val):
    if key in target_dict.keys() and val >= target_dict[key]:
        return True;
    else:
        return False;

# Populate Map
def update_RAM(coords, size):
    grid = [(["."]*(size[1]+1)) for i in range(size[0]+1)];

    # populates the grid with the time
    for block in coords:
        grid[block[0]][block[1]] = "#";

    return grid;

def in_grid(grid, loc):
    ''' Checks that the location loc is within grid bounds '''
    if (loc[0] >= 0 and loc[0] < len(grid) and
        loc[1] >= 0 and loc[1] < len(grid[0])):

        return True;
    return False;

# Dijkstra
def dijkstra(maze, start, end, lowest, loc_dir = {}):
    # visited = set();
    queue = [];
    heapq.heappush(queue, (0, start, (0,1))); # time, distance, position, direction

    while queue:
        dist, current, curr_dir = heapq.heappop(queue);

        if current == end and dist <= lowest:
            lowest = dist;

        # for some reason this only works if check_dict_dist is modified [likely due to same weightage for any branch]
        if check_dict_dist(loc_dir, (current, curr_dir), dist): continue;
        else: loc_dir[(current, curr_dir)] = dist;

        """ if (current, curr_dir) in visited: continue;
        
        visited.add((current, curr_dir)); """
        
        next_dirs = [curr_dir, DIRS[(DIRS.index(curr_dir)+1)%4], DIRS[(DIRS.index(curr_dir)+3)%4]];

        for heading in next_dirs:
            next_pos = (current[0]+heading[0], current[1]+heading[1]);
        
            if in_grid(maze, next_pos) and maze[next_pos[0]][next_pos[1]] != "#":
                heapq.heappush(queue, (dist+1, next_pos, heading));

    return lowest;

############################ MAIN ######################################
coords = [];

with open("FallingBytes.txt") as f:
    data = f.read().splitlines();

    for line in data:
        coords.append([int(num) for num in line.split(",")][::-1]);

########################### Part 2 #####################################
sec1 = time.time();
maze = update_RAM(coords[:1024], size = (70,70));
part1 = dijkstra(maze, start = (0,0), end = (70,70), lowest = 10**8);
print("Part 1:", part1, " Time:", round(time.time() - sec1, 4));

########################### Part 2 #####################################
i = 1024;
target = 0;
sec2 = time.time();

while(target != 10**8):
    i += 1;
    maze = update_RAM(coords[:i], size = (70,70));
    target = dijkstra(maze, start = (0,0), end = (70,70), lowest = 10**8, loc_dir = {});

print("Part 2:", coords[i-1][::-1], "Time:", round(time.time() - sec2, 4))