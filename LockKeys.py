# AoC Day 25 - Locks and Keys

keys, locks = [], [];

with open("LockKeys.txt") as f:
    data = f.read().splitlines();
    i = 0;

    while(i < len(data)):
        target = keys if "." in data[i] else locks;
        target.append([0]*len(data[0]));
        i += 1;
        
        for _ in range(5):
            for j in range(len(data[i])):
                target[-1][j] += 1 if data[i][j] == "#" else 0;
            i += 1;
        i += 2;

count = 0;

for key in keys:
    for lock in locks:
        if all(num <= 5 for num in [sum(x) for x in zip(key, lock)]): 
            count += 1;

print(count)