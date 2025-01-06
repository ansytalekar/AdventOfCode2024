# Find distance between two lists of same length
ids1 = [];
ids2 = [];

with open("DistList.csv") as f:
    data = f.readlines();

    for line in data:
        ids = line.split();
        ids1.append(float(ids[0]));
        ids2.append(float(ids[1]));

def find_min(ids):
    holder = ids[0];
    
    for i in ids:
        if holder > i:
            holder = i
        else:
            continue;

    return holder;

dist = 0;

for i in range(len(ids1)):
    min1 = find_min(ids1)
    min2 = find_min(ids2)
    ids1.remove(min1)
    ids2.remove(min2)

    dist += abs(min1-min2);

print(dist)