''' Leaving comments and suggestions in orange - Yash '''

f=open('Rules_Print.txt','r')
wordblock = []

for line in f:
    wordblock.append(line.strip())
data='|'.join(wordblock)
input=data.split("|")

input1=[]
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
for i in range(0,2352):
    input1.append(int(input[i]))

list=[]
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
for i in range(0,2352):
    list.append(int(input1[i]))

# print(input1)
# quit()

for i in range(len(list)):
    counter=0
    for j in range(len(list)):
        if list[j]:
            if list[i]==list[j]:
                counter +=1
                if counter>1:
                    list[j]='removeme'

list = [value for value in list if value != "removeme"]
print(list)

for i in range(0, 2352, 2):
    first_value = input1[i]
    second_value = input1[i + 1] 
    inserted=False
    
    j=0
    while j < len(list):  
        if list[j] == second_value and not inserted:
            list.insert(j, first_value)
            inserted = True
            j += 1  
        j += 1  

        counter = 0
        for l in range(len(list)):
            if list[l] == first_value:
                counter += 1
                if counter > 1:  
                    list[l] = 'removeme'
    list = [value for value in list if value != 'removeme']

reversedlistcopyupdated=list
print(reversedlistcopyupdated)
quit()

updates=[]
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
for i in range(2352+1,len(input)):
    updates.append(input[i])

niceupdates=[]
for i in updates: 
    niceupdates.append([int(x) for x in i.split(',')])
def checker(update,correctorder):
    copy=correctorder.copy()
    for i in range(0,len(correctorder)):
        counter=0
        for j in range(0,len(update)):
            if correctorder[i]==update[j]:
                counter+=1

        if counter==0:
            copy[i]='removeme'
           
    copyupdated= [value for value in copy if value != "removeme"]

    counter=0
    for i in range(0,len(copyupdated)):
        if copyupdated[i]==update[i]:
            counter+=1
    if counter==len(update):
        return update

yes=[]
for i in range(0,len(niceupdates)):
    yes.append(checker(niceupdates[i],reversedlistcopyupdated))

yess=[value for value in yes if value is not None]
#print(yess)
import math
b=[]
# find the middle values: 
for i in range(0,len(yess)):
    b.append(yess[i][math.ceil(len(yess[i])/2)-1])


#add it all up:
answer=sum(b)
print(answer)