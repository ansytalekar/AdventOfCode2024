#getting the list of numbers in the right order
input1=[]
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
for i in range(0,2352):
    input1.append(int(input[i]))
#print(input1)

list=[]
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
for i in range(1,2352,2):
    list.append(int(input1[i]))
#print(list)

for i in range(0, len(input1), 2):
    first_value = input1[i]
    second_value = input1[i + 1] 

    j = 0
    while j < len(list):  
        if list[j] == second_value:
            list.insert(j, first_value)
            j += 1  
        j += 1  

#print(list)


reversedlistcopy=list.copy()
for i in range(len(list)):
    counter=0
    for j in range(len(list)):
        if reversedlistcopy[j]:
            if list[i]==reversedlistcopy[j]:
                counter +=1
                if counter>1:
                    reversedlistcopy[j]='removeme'
#print(reversedlistcopy)
reversedlistcopyupdated = [value for value in reversedlistcopy if value != "removeme"]
#print(reversedlistcopyupdated)

# remove the none values: 
yess=[value for value in yes if value is not None]
#print(yess)
import math
b=[]
# find the middle values: 
for i in range(0,len(yess)):
    b.append(yess[i][math.ceil(len(yess[i])/2)-1])

print(b)

#add it all up:
answer=sum(b)
print(answer)
