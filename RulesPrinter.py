# Recursive loop checker for Day 5 Advent
class LoopChecker:
    def __init__(self):
        self.storage = set();
        self.recursive = set();

    def loop_check(self, rules_dict, rule, storage, recursive):
        storage.add(rule);
        recursive.add(rule);

        for component in rules_dict[rule]:
            if component not in storage:
                if self.loop_check(rules_dict, component, storage, recursive):
                    return True;
            elif component in recursive:
                return True;

        recursive.remove(rule);
        return False;

    def strip_dict(self, rules):
        for rule in rules:
            if rule not in self.storage:
                if self.loop_check(rules, rule, self.storage, self.recursive):
                    return True;
        
        return False;

############################################################################################

# checks if line is valid
def check_line(rules, line):
    # Reverses order to do forward searching
    line = line[::-1];

    # loops through the line
    for i in range(len(line)):
        # checks if the number is in the rules dict (otherwise no need to check terms after)
        if line[i] in rules.keys():
            # loops through terms after the current position
            for val in line[(i+1):]:
                # if rule is violated breaks out
                if val in rules[line[i]]:
                    return False;
                else:
                    pass
        # if not in rules, it doesn't need to search for no reason
        else:
            continue;

    # if it passes without returning False
    return True;

# returns the middle number of the fixed list
def fix_line(rules, line, show = False):
    # stores first number
    fix_arr = [];
    
    # checks for next numbers in array
    for num in line:
        # if not in rules, add it to the end [not to the beginning, because another rule may be violated]
        if num in rules.keys():
            # loop check, number could be in rules, but not added yet
            added = False;

            # loops through fixed array to check where to place num
            for i in range(len(fix_arr)):
                if fix_arr[i] in rules[num]:
                    if show:
                        print(f"{num}|{fix_arr[i]}")
                    fix_arr = fix_arr[0:i] + [num] + fix_arr[i:];
                    added = True;
                    break;

            # adding number if finished loop but not added
            if not added:
                fix_arr.append(num);

        else:
            fix_arr.append(num);

    # returns the fixed array
    return fix_arr;

################################################################

rules = {};
published = [];

# reading lines
with open("Rules_Print.txt") as f:
    lines = f.read().splitlines();
    switch = 0;

    for line in lines:
        if len(line) == 0:
            switch = 1;
            continue;

        if switch == 0:
            nums = line.split("|"); 

            if int(nums[0]) in rules.keys():
                rules[int(nums[0])].append(int(nums[1]));
            else:
                rules[int(nums[0])] = [(int(nums[1]))];
    
        else:
            published.append([int(i) for i in line.split(",")])

middle_sum = 0;
middle_sum2 = 0;

for line in published:
    if check_line(rules, line):
        middle_sum += line[(len(line)//2)]
    else:
        fixed_line = fix_line(rules, line);
        middle_sum2 += fixed_line[(len(fixed_line)//2)]

print(middle_sum)
print(middle_sum2)

checker = LoopChecker()
print(checker.strip_dict(rules = rules))

# damini_in = [75, 21, 28, 29, 73, 95, 48, 19, 16, 81, 51, 56, 59, 83, 64, 57, 86, 15, 43, 82, 49, 31, 35, 68, 26, 63, 69, 84, 47, 23, 18, 87, 53, 79, 34, 85, 94, 78, 65, 88, 45, 76, 39, 92, 67, 89, 66, 62, 27];
# print(fix_line(rules, damini_in, True));
