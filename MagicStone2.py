import time;
from matplotlib import pyplot as plt;

input = "6563348 67 395 0 6 4425 89567 739318";
# input = "7725 185 2 132869 0 1840437 62 26310";

stone_ocean = {}; # cheeky jojo reference

def stones(stones):
    new_stones = {};

    for num in stones.keys():
        # print(num)

        if num == 0:
            add_to_dict(new_stones, 1, stones[0]);
        
        elif len(str(num)) % 2 == 0:
            new_num = str(num)
            num1 = int(new_num[:len(new_num)//2])
            num2 = int(new_num[len(new_num)//2:])
            add_to_dict(new_stones, num1, stones[num]);
            add_to_dict(new_stones, num2, stones[num]);

        else:
            add_to_dict(new_stones, num*2024, stones[num]);
    
        # print(stones, "\n", new_stones)

    return new_stones;

def add_to_dict(stones, key, val):
    if key in stones.keys():
        stones[key] += val; 
    else:
        stones[key] = val;

############################ Main #######################################

for digit in [int(dig) for dig in input.split()]:
    if digit in stone_ocean.keys():
        stone_ocean[digit] += 1;
    else:
        stone_ocean[digit] = 1;
    
distinct_count = [len(stone_ocean.keys())];

loops = 75;

sec = time.time();
for i in range(loops):
    stone_ocean = stones(stone_ocean)
    # distinct_count.append(len(stone_ocean.keys()))

count = 0;

for key in stone_ocean.keys():
    count += stone_ocean[key];

""" plt.plot(range(loops+1), distinct_count);
plt.xlabel("Number of Blinks");
plt.ylabel("Number of Distinct Stones");
plt.title("Distinct Stones per Blink");
plt.grid(which="both");
plt.show() """

print("Final stone count:", count);
print(time.time() - sec)