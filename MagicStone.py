import time

input = "6563348 67 395 0 6 4425 89567 739318";
# input = "7725 185 2 132869 0 1840437 62 26310";

arr = [int(digit) for digit in input.split()];

# magic stones calculator
def stones(arr):
    new_arr = [];

    if isinstance(arr, int):
        arr = [arr]

    for digit in arr:
        if digit == 0:
            new_arr.append(1);
        
        elif len(str(digit)) % 2 == 0:
            new_num = str(digit)
            num1 = int(new_num[:len(new_num)//2])
            num2 = int(new_num[len(new_num)//2:])
            new_arr.append(num1)
            new_arr.append(num2)

        else:
            new_arr.append(digit*2024);

    return new_arr;

# for faster array handling
def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

loops = 75;
branches = False;

sec = time.time()
for i in range(loops):
    print(i)
    new_arr = [];

    if branches:
        for line in arr:
            push = stones(line);
    
            if len(push) > 2000:
                push = split(push, 2000);
    
            for input in push:
                new_arr.append(input)

    else:
        push = stones(arr);
        
        if len(push) > 2000:
            new_arr = split(push, 2000);
            branches = True;
        else:
            new_arr = push;

    arr = new_arr;

stone_count = 0;

for line in arr:
    if isinstance(line, int):
        line = [line]

    stone_count += len(line);

print(stone_count)
print(time.time() - sec)