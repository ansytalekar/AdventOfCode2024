# Day 22 - Secret Numbers
import copy;
from functools import cache;

@cache
def update_num(num):
    new_num = ((num*64) ^ num) % 16777216;
    new_num = (int(new_num/32) ^ new_num) % 16777216;
    new_num = ((new_num*2048) ^ new_num)  % 16777216;
    return new_num;

def recreate(arr):
    new_arr = [];
    
    for num in arr:
        new_arr.append(update_num(num));

    return new_arr;

def add_to_dict(target_dict, key, val):
    if key in target_dict.keys():
        target_dict[key] += val;
    else:
        target_dict[key] = val;

################# MAIN #################
secrets = [int(code) for code in open("SecretNums.txt").read().splitlines()];

secret_sum = 0;
banana_republic = {};

for num in secrets:
    new_secrets = [num, update_num(num)]

    for i in range(1999):
        new_secrets.append(update_num(new_secrets[-1]));

    secret_sum += new_secrets[-1];
    price_change = [(p2 % 10 - p1 % 10) for (p2, p1) in zip(new_secrets[1:], new_secrets[:-1])];

    seen = set();

    for i in range(len(new_secrets) - 4):
        seq = tuple(price_change[i:i+4]);

        if seq not in seen:
            add_to_dict(banana_republic, seq, new_secrets[i+4] % 10);
            seen.add(seq);
    
print(f"Part 1: {secret_sum}", f"Part 2: {max(banana_republic.values())}");

############## GRAVEYARD ##############
""" new_secrets = [secrets];
price_change = [];

for i in range(2000):
    new_secrets.append(recreate(new_secrets[-1]));
    price_change.append([(p2 % 10 - p1 % 10) for (p2, p1) in zip(new_secrets[-1], new_secrets[-2])]);

print(f"Part 1: {sum(new_secrets[-1])}");

################ PART 2 ################
banana_republic = {};
new_secrets = list(zip(*new_secrets));
price_change = list(zip(*price_change));

for trader in price_change:
    seen = set();
    for i in range(len(trader)-4):
        seq = tuple(trader[i:i+4]);

        if seq not in seen:
            add_to_dict(banana_republic, seq, new_secrets[price_change.index(trader)][i+4] % 10);
            seen.add(seq);

print(max(banana_republic.values())); """