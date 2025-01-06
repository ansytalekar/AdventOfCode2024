# AoC Day 19
def add_to_dict(target_dict, key, val) -> None:
    if key in target_dict.keys() and val not in target_dict[key]:
        target_dict[key].append(val);
    else:
        target_dict[key] = [val];

def check_design(word, length, towels):
    if len(word) in towels.keys() and word in towels[len(word)]:
        return True;
    elif length == 0:
        return False;
    else:
        if length in towels.keys():
            check_in = towels[length];
        else:
            return check_design(word, length - 1, towels);

    for pattern in check_in:
        if pattern in word:

            checks = [];
            splits = [s for s in word.split(pattern) if s];

            for split in splits:
                checks.append(check_design(split,len(split),towels));

            if all(checks):
                add_to_dict(towels, len(word), word);
                return True;
        else:
            continue;
    
    return check_design(word, length - 1, towels);

###################################### MAIN ######################################
towels = {};

with open("Towels.txt") as f:
    data = f.read().splitlines();

    # arranging towels into dictionaries based on pattern lengthA
    patterns = data[0].split(", ");

    for pattern in patterns:
        add_to_dict(towels, len(pattern), pattern)

    # desired towel arrangements
    designs = data[2:];

count = 0;

for i in range(len(designs)): # design in designs:
    print(i)
    design = designs[i];
    count += check_design(design, max(towels.keys()), towels);

print(count)