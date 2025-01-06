f=open('ReindeerMaze.txt','r')
 
count = 0
 
def checker(Square_current, wordblock, count, Direction, dictionary):
    Square_new = (Square_current[0] + Direction[0], Square_current[1] + Direction[1])  
    if Square_new == ("E"):
        return
 
    squareE = ((-1,0),(1,0))
    squareN = ((0,-1),(0,1))
 
    if (Square_current[0], Square_current[1]) in dictionary:
        # If the current square has already been visited with fewer steps, return early
        if dictionary[(Square_current[0], Square_current[1])] <= count:
            return

    # Update the dictionary with the current square's step count
    dictionary[(Square_current[0], Square_current[1])] = count
    # Mark the square in the wordblock with the current count
    wordblock[Square_current[0]][Square_current[1]] = count
 
    if wordblock[Square_new[0]][Square_new[1]] != "#":
        checker(Square_new, wordblock, count + 1, Direction, dictionary)
    # Directions to move in the maze
   
    if Direction in squareN:
        square = squareE
    else:
        square = squareN
    # Explore all four possible directions
 
    for dx, dy in square:
        Square_new = (Square_current[0] + dx, Square_current[1] + dy)
 
        # Skip invalid squares (out of bounds or walls)
        if wordblock[Square_new[0]][Square_new[1]] == "#":
            continue
       
        # If the target square is the bottom-right corner, return immediately
        if Square_new == ("E"):
            return
       
        # Check if the square is already visited with fewer steps
        if Square_new in dictionary and dictionary[Square_new] <= count + 1001:
            continue
       
        # Increment step count and recurse for valid squares
        checker(Square_new, wordblock, count + 1001,(dx,dy), dictionary)
 
wordblock = []
linearr = []
dictionary = {}
 
row = 0
for line in f:
    linearr = []
    columb = 0
    for digit in line:
        if digit != "\n":
            linearr.append(digit)
        if digit == "S":
            Square_new = (row,columb)
        columb += 1
    row += 1
    wordblock.append(linearr)
checker(Square_new,wordblock,0,(0,1),dictionary)
 
g=open("TESTERRRRRR222.txt","w")
for line in wordblock:
    for half in line:
        g.write(str(half))
        g.write("      ")
    g.write("\n")
g.close