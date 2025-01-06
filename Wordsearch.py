
# Wordsearch
import math
import time

# Stores position of word and direction index
pos_dir_index = {};

# Overarching wordsearch function
def find_word(wordsearch, word):
    occurences = 0;

    for i in range(len(wordsearch)):
        for j in range(len(wordsearch[0])):
            if(wordsearch[i][j] == word[0]):
                occurences += check_start(wordsearch, word, (i,j))

    # Return count
    return(occurences)

# Checks in different directions
def check_start(wordsearch, word, start_pos):
    directions = [[-1,1], [0,1], [1,1], [-1,0], [1,0], [-1,-1], [0,-1], [1,-1]]
    # directions = [[-1,1], [1,1], [-1,-1], [1,-1]]

    # Iterate through directions and check for the word
    # Occurences records number of times word appears
    occurences = 0;
    
    for dirs in directions:
        if (check_word(wordsearch, word, start_pos, dirs)):
            occurences += 1;
		
            if start_pos in pos_dir_index.keys():
                pos_dir_index[start_pos].append(tuple(dirs));
            else:
                pos_dir_index[start_pos] = [tuple(dirs)];

    return occurences

# Checks specified direction for word
def check_word(wordsearch, word, start_pos, dir):
    found_ltrs = word[0];
    current_pos = start_pos;

    while (found_ltrs in word[0:len(found_ltrs)]):
        if(len(found_ltrs) == len(word)):
            # Returns true if length mtches
            return True;

        # Keep searching
        current_pos = [current_pos[0] + dir[0], current_pos[1] + dir[1]]

        if (current_pos[0] < len(wordsearch) and current_pos[1] < len(wordsearch[0])) and (current_pos[0] >= 0 and current_pos[1] >= 0):
            found_ltrs += wordsearch[current_pos[0]][current_pos[1]];
        else:
            # Reached edge of wordsearch and not found word
            return

##########################################################################################################

def cross_share(pos_dir_index, word):
    cross_counts = 0;
    indexes = pos_dir_index.keys();

    rules = {(1,1): (1,-1), (-1,1): (-1,-1)} # rows
    rules2 = {(1,1): (-1,1), (1,-1): (-1,-1)} # columns
    
    for keys in indexes:    
        for i in range(1, len(word)-1):
            next_key = (keys[0], keys[1]+2*i);
            
            if next_key in indexes:
                pairs1 = pos_dir_index[keys];
                pairs2 = pos_dir_index[next_key];

                for p in pairs1:
                    if p in rules and rules[p] in pairs2:
                        cross_counts += 1;

            next_key2 = (keys[0]+2*i, keys[1]);
            
            if next_key2 in indexes:
                pairs1 = pos_dir_index[keys];
                pairs2 = pos_dir_index[next_key2];

                for p in pairs1:
                    if p in rules2 and rules2[p] in pairs2:
                        cross_counts += 1;

    return cross_counts;


##########################################################################################################

# import wordsearch
with open("Wordsearch.txt", "r") as f:
    wordsearch = f.read().splitlines();

# find word count
counts = find_word(wordsearch, "XMAS");
print(counts)
print(cross_share(pos_dir_index, "XMAS"))