import re;
import heapq;

# Dijkstra's Algorithm learnt from https://www.youtube.com/watch?v=_B5cx-WD5EA

# DIRS = {(0, 1): (0,-1), (1,0): (-1,0), (0,-1): (0,1), (-1,0): (1,0)};
DIRS = [(0,1), (-1,0), (0,-1), (1,0)];

# Non Dijkstra [has a recursive limit]
def walk_maze(maze, pos, curr_dir, pos_dir = []):
    score = [];
    next_dir = [];
    pos_dir.append(pos);

    next_dir = [DIRS[dir] for dir in DIRS if dir != curr_dir];

    for dir in DIRS.keys():
        if dir != curr_dir:
            next_dir.append(DIRS[dir])

    for dir in next_dir:
        new_pos = (pos[0]+dir[0], pos[1]+dir[1]);

        if new_pos not in pos_dir:
            if(maze[new_pos[0]][new_pos[1]] == "."):
                score.append(walk_maze(maze, new_pos, dir, pos_dir));
            
                if dir == curr_dir:
                    score[-1] += 1;
                else:
                    score[-1] += 1001;

            elif(maze[new_pos[0]][new_pos[1]] == "E"):
                return 1;
        else:
            continue;
    
        if new_pos in pos_dir:
            pos_dir.remove(new_pos);
    
    if len(score) == 0: score = [(len(maze)*1000)**2]
    return min(score);

# Check dictionary
def check_dict_dist(target_dict, key, val):
    if key in target_dict.keys() and val > target_dict[key]:
        return True;
    else:
        return False;

# Dijkstra
def dijkstra(maze, start, end, lowest, part2_dir = {}):
    # visited = set();    <-- used for part 1
    queue = [];
    unique_seats = set();
    heapq.heappush(queue, (0, start, (0,1), [start])); # position, distance, direction

    while queue:
        dist, current, curr_dir, path = heapq.heappop(queue);
        
        if current == end and dist <= lowest:
            lowest = dist;
            unique_seats.update(path);
        
        # Dijkstra's Part 1: [fails part2 cause thinks node already visited, doesn't minimze all paths]
        """ if (current, curr_dir) in visited:
            continue;

        visited.add((current, curr_dir)); """

        if check_dict_dist(part2_dir, (current, curr_dir), dist): continue;
        else: part2_dir[(current, curr_dir)] = dist;
        
        next_dirs = [dir for i, dir in enumerate(DIRS) if i != (DIRS.index(curr_dir) + 2) % 4];

        for heading in next_dirs:
            next_pos = (current[0]+heading[0], current[1]+heading[1]);
        
            if maze[next_pos[0]][next_pos[1]] != "#" and heading == curr_dir:
                heapq.heappush(queue, (dist+1, next_pos, heading, path + [next_pos]));
            elif maze[next_pos[0]][next_pos[1]] != "#":
                heapq.heappush(queue, (dist+1001, next_pos, heading, path + [next_pos]));

    return lowest, len(unique_seats);

##################### Main ########################
maze = [];
# additional values for start_pos 

with open("Advent_16.txt") as f:
    lines = f.read().splitlines()
    
    for i in range(len(lines)):
        maze.append([ltr for ltr in lines[i]]);
        if "S" in lines[i]: start_pos = (i, re.search("S", lines[i]).start());
        if "E" in lines[i]: end_pos = (i, re.search("E", lines[i]).start());

s1 = dijkstra(maze, start_pos, end_pos, (len(maze)*len(maze[0]))**2);
print(f"Part 1: {s1}");
s2 = dijkstra(maze, start_pos, end_pos, s1[0]);
print(f'Part 2: {s2}');