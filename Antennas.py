def check_antinodes(loc1, loc2, size, nodes):
    x_dist = loc2[0] - loc1[0];
    y_dist = loc2[1] - loc1[1];

    count = 0;

    test1 = (loc1[0] - x_dist, loc1[1] - y_dist);
    test2 = (loc2[0] + x_dist, loc2[1] + y_dist);

    if ((test1[0] >= 0 and test1[0] < size[0]) and
        (test1[1] >= 0 and test1[1] < size[1]) and 
        test1 not in nodes):
        count += 1;
        nodes.append(test1);
    
    if ((test2[0] >= 0 and test2[0] < size[0]) and
        (test2[1] >= 0 and test2[1] < size[1]) and 
        test2 not in nodes):
        count += 1;
        nodes.append(test2);
    
    return count;

def check_harmonics(loc1, loc2, size, nodes):
    m = (loc2[1] - loc1[1])/(loc2[0] - loc1[0]);

    count = 0;
    x = 0;
    while x < size[0]:
        y_pos = m*(x - loc1[0]) + loc1[1];

        if (y_pos < size[1] and y_pos >= 0 and
        (y_pos*10)%10 == 0 and (x, y_pos) not in nodes):
            nodes.append((x, y_pos));
            count += 1;

        x += 1;

    return count;


################################################################################
# Main

# Dictionary generation from file
input = {};
nodes = [];
nodes2 = [];

# Said file
with open("Antenna.txt") as f:
    lines = f.read().splitlines();

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] != ".":
                if lines[i][j] in input.keys():
                    input[lines[i][j]].append((i,j));
                else:
                    input[lines[i][j]] = [(i,j)];

size = [i+1, j+1]

# holding puzzle results
antinodes = 0;
harmonics = 0;

for key in input.keys():
    locs = input[key];
    
    for i in range(len(locs)-1):
        for pos2 in locs[i+1:]:
            antinodes += check_antinodes(locs[i], pos2, size, nodes)
            harmonics += check_harmonics(locs[i], pos2, size, nodes2);

print(antinodes)
print(harmonics)