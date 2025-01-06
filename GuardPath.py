import copy;
from copy import deepcopy;
import time;

class GuardPath:
    def __init__(self, map_txt):
        self.map_txt = map_txt;
        self.loop = False;
        self.start_pos = [];
        self.obs_dict = {};
        self.dir = [-1,0];

        for i in range(len(self.map_txt)):
            # finding starting pos
            for j in range(len(self.map_txt[0])):
                if self.map_txt[i][j] == "^":
                    self.start_pos = [i,j];

    def return_looper(self):
        if self.loop:
            return False;
        return True;

    # check for in grid
    def in_grid(self,pos):
        ''' Array is the input sequence, pos is the position of the guard '''
        # size = arr.shape;

        size = [len(self.map_txt), len(self.map_txt[0])]

        for i in range(len(size)):
            if (pos[i] < 0 or pos[i] >= size[i]):
                return False;
            
        return True;

    def check_loop(self, pos):
        if pos in self.obs_dict.keys():
            if tuple(self.dir) in self.obs_dict[pos]:
                return True;
            else:
                self.obs_dict[pos].append(tuple(self.dir))
        
        else:
            self.obs_dict[pos] = [tuple(self.dir)]
            return False;

    def walk_grid(self):
        steps = 0;
        looping = 0;
        path = [];

        # walk grid
        while(True):
            steps += 1;
            path.append(tuple(self.start_pos))

            next_pos = [self.start_pos[0] + self.dir[0], self.start_pos[1] + self.dir[1]];

            self.map_txt[self.start_pos[0]][self.start_pos[1]] = "X";
            
            if self.in_grid(next_pos):
                while(self.map_txt[next_pos[0]][next_pos[1]] == "#" or self.map_txt[next_pos[0]][next_pos[1]] == "O"):
                    if self.check_loop(tuple(next_pos)):
                      looping = 1;
                      break;
                    
                    self.dir = [self.dir[1], -self.dir[0]];
                    next_pos = [self.start_pos[0] + self.dir[0], self.start_pos[1] + self.dir[1]];
                
                if self.map_txt[next_pos[0]][next_pos[1]] == "X":
                    steps -= 1;
            
                self.map_txt[next_pos[0]][next_pos[1]] = "^";
            
            else:
                break;   

            self.start_pos = next_pos;

        return steps, looping, path;
#######################################################################################
# Main
map_txt = []

# reading lines
with open("Map.txt") as f:
    lines = f.read().splitlines();

    for line in lines:
        map_txt.append([str for str in list(line)]);

guard = GuardPath(copy.deepcopy(map_txt));
res1 = guard.walk_grid()
print(res1[0]);

loop_count = 0;

seconds = time.time();

for i in range(len(map_txt)):
    for j in range(len(map_txt[0])):
        if map_txt[i][j] == "^" or map_txt[i][j] == "#":
            continue;
        elif (i,j) not in res1[2]:
            continue;
        else:
            map_txt[i][j] = "O";
            guard2 = GuardPath(copy.deepcopy(map_txt));
            loop_count += guard2.walk_grid()[1];
            map_txt[i][j] = ".";

print(loop_count)
print(time.time() - seconds);