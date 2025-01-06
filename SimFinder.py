from collections import Counter

# Find number of occurences
ids1 = [];
ids2 = [];

with open("DistList.csv") as f:
    data = f.readlines();

    for line in data:
        ids = line.split();
        ids1.append(float(ids[0]));
        ids2.append(float(ids[1]));

sim_score = 0;

for i in ids1:
    holder = ids2.count(i);

    sim_score += i*holder;

print(sim_score)