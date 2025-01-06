import re;
import time;
import matplotlib.pyplot as plt;
import numpy as np;
import math;

robots = {};
part2 = True; # switch for part 1 or part 2

def hop(pos, vel, step, size):
    new_pos = [];

    for i in range(len(pos)):
        new_pos.append((pos[i]+step*vel[i]) % size[i]);

    return tuple(new_pos)

with open("Robots.txt") as f:
    lines = f.readlines();

    for i in range(len(lines)):
        data = re.findall(r"-?\d+", lines[i])
        robots[i] = [(int(data[1]), int(data[0])), (int(data[3]),int(data[2]))];
        
size = (103,101);    
loops = 100 if part2 else 1;
step = size[0] if part2 else 100; # change as needed

for i in range(0, loops):
    # visualizing
    plt.clf();
    grid = np.zeros(size);

    for key in robots.keys():
        new_pos = hop(robots[key][0], robots[key][1], i*step + 43 if part2 else step, size)
        robots[key][0] = robots[key][0] if part2 else new_pos;
        grid[new_pos[0], new_pos[1]] = 255;

    plt.imshow(grid, cmap='viridis')
    plt.title(f"Iteration {i*step + 43 if part2 else step}");
    plt.pause(0.05);
    time.sleep(0.45);

quit() if part2 else time.sleep(1);

# only part 1 
count = [0,0,0,0,0];

for key in robots.keys():
    pos = robots[key][0];

    count[0] += (pos[0] < size[0]//2 and pos[1] < size[1]//2)       # top left   
    count[1] += (pos[0] < size[0]//2 and pos[1] > size[1]//2)       # top right
    count[2] += (pos[0] > size[0]//2 and pos[1] < size[1]//2)       # bottom left
    count[3] += (pos[0] > size[0]//2 and pos[1] > size[1]//2)       # bottom right
    count[4] += (pos[0] == size[0]//2 and pos[1] == size[1]//2)     # matches middle

safety = math.prod(count[:-1]);

print(safety);

# x: 42,145,248 --> patterns follow 103x+42   [ integer match at 6531 ]
# y: 67,168,269 --> patterns follow 101x+67   [ integer match at 6531 ]   + 1 second for starting from 0