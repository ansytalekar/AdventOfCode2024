# Method 1
def check_perms(val, arr, oper, target):
    ''' Forward searches through the arr '''
    # if value exceeded, auto DSQ
    if val > target:
        return False;

    # otherwise checks if value met when array is empty
    if len(arr) == 0 and val == target:
        return True;
    elif len(arr) == 0:
        return False;
    # otherwise recursive down based on operator
    else:
        if oper == "+":
            val += arr[0];
        elif oper == "*":
            val *= arr[0];
        elif oper == "|":
            val = int(str(val) + str(arr[0]));

        return (check_perms(val, arr[1:], "+", target) or check_perms(val, arr[1:], "*", target) or check_perms(val, arr[1:], "|", target));

# Method 2
def check_tree(target, arr):
    ''' Backward searches through the arr '''
    # if 0, then automatic DSQ
    if target < 0:
        return False;
    # when only one value in array, check if matching target
    if len(arr) == 1:
        if target == arr[0]:
            return True;
        else:
            return False;
    # otherwise recursive check
    else:
        # only divide if remainder 0
        if target % arr[-1] == 0:
            if check_tree(int(target/arr[-1]), arr[:-1]):
                return True;
        # else subtract, the 1st condition above catches any below 0
        if check_tree(target-arr[-1], arr[:-1]):
            return True;
        else:
        # checks for concat (might be faster to make this the if instead)
            str_target = str(target);
            arr_target = str(arr[-1]);

            if (not (len(str_target) <= len(arr_target))) and (int(str_target[-len(arr_target):]) == arr[-1]):
                return check_tree(int(str_target[:-len(arr_target)]), arr[:-1]);
            else:
                return False;

################################################################################
# Main

# Dictionary generation from file
input = {};
with open("Calbirators.txt") as f:
    lines = f.read().splitlines();

    for line in lines:
        data = line.split(":");

        input[int(data[0])] = [int(i_str) for i_str in data[1].split()]

# Variables to store sum and check lines for both methods [Method 1 worked first]
store_sum = 0;
store_sum2 = 0;
works1 = [];
works2 = [];
brokeon = [];

# Iterating over each line
for key in input.keys():
    try:
        # Method 2
        if check_tree(key, input[key]):
            store_sum += key;
            works1.append(key);
        # Method 1
        if (check_perms(input[key][0], input[key][1:], "+", key) or check_perms(input[key][0], input[key][1:], "*", key) or
        check_perms(input[key][0], input[key][1:], "|", key)):
            store_sum2 += key;
            works2.append(key);
    # Error Handling to fix Method 2 issues
    except Exception as e:
        print(e)
        brokeon.append(key);

# Results and comparison
print(store_sum, store_sum2)
""" print("Missing in back recurs", (set(works2).difference(works1)));
print(brokeon) """