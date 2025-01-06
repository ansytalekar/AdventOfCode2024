''' Yash's Reworking of Damini's'''
import re

# opens file
with open('MulList.txt', 'r') as f:
    file = f.readlines();

    file_onetxt = ''.join(l.rstrip() for l in file);

# split by don't
don_split = file_onetxt.split("don't()");

b = []
for line in don_split[1:]:
    m = re.findall(r'do\(\).*', line)
    m2 = ''.join(m)

    if m:
        b.append(m2)
    else:
        pass

f = [0];
for line in b:
    am = re.findall(r"mul\(\d+,\d+\)", line);

    add = 0;

    for run in am:
        run2 = run.replace('mul(', '').replace(')', '');
        val1, val2 = run2.split(",")
        add += int(val1)*int(val2);

    f.append(add)

print(f)

g=0;
am2 = re.findall(r"mul\(\d+,\d+\)", don_split[0]);
for run in am2:
    run2 = run.replace('mul(', '').replace(')', '');
    val1, val2 = run2.split(",")
    g += int(val1)*int(val2);

print(g)
print(sum(f))
quit()

''' Damini's Code '''
import re

# opens file
f = open('MulList.txt','r')
file=f.readlines()
string=''.join(file)
 
# splits string by don't()
a=string.split("don't()")

b=[]
for i in range(len(a)):
    m=re.search(r'do\(\).*',a[i])

    if m:
        b.append(m.group())
    else:
        pass

bs=''.join(b)
am=bs.split('mul(')
 
j=[]
for i in range(0,len(am)):
    if am[i][0].isdigit():
        j.append(am[i])
    else:
        pass
 
c=[]
for i in range(len(j)):
    match=re.search(r'^\d+,\d+\)',j[i])
    if match:
        c.append(match.group())
    else:
        pass
 

d=[]
for i in range(len(c)):
    match=re.search(r'^\d+,\d+',c[i])
    if match:
        d.append(match.group())
    else:
        pass

 
for i in range(len(d)):
    d[i]=d[i].split(',')
 

 
    
#do the multiplitcation 
e=[]
for i in range(len(d)):
    e.append(int(d[i][0])*int(d[i][1]))

 
# do the adding
f=0
for i in range(len(e)):
    f+=e[i]
print(f)
 
z=a[0]

 
 
a=z.split('mul(')
 
b=[]
for i in range(0,len(a)):
    if a[i][0].isdigit():
        b.append(a[i])
    else:
        pass

 
c=[]
for i in range(len(b)):
    match=re.search(r'^\d+,\d+\)',b[i])
    if match:
        c.append(match.group())
    else:
        pass
 

d=[]
for i in range(len(c)):
    match=re.search(r'^\d+,\d+',c[i])
    if match:
        d.append(match.group())
    else:
        pass
 
for i in range(len(d)):
    d[i]=d[i].split(',')

 
    
#do the multiplitcation 
e=[]
for i in range(len(d)):
    e.append(int(d[i][0])*int(d[i][1]))
print(e)
 
# do the adding
g=0
for i in range(len(e)):
    g+=e[i]
print(g)
 
answer=f+g
print(answer)