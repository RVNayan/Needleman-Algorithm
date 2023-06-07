import numpy as np
import matplotlib.pyplot as pt
A='atgc'
B='atgctc'

s2 = list(' '+B)
s1 = list(' '+A)
h = s1

hle= list(np.linspace(0,-(len(s1)-1)*2,len(s1)))
vle = list(np.linspace(0,-(len(s2)-1)*2,len(s2)))
# print(len(hle),len(s1))

M=[]
M.append(s1)
M.append(hle)
for i in range(1,len(vle)):
    m=[]
    m.append(vle[i])
    for j in range(len(hle)-1): #-1 to prevent extra spaces at the end
        m.append('')
    M.append(m)


def check(Matrix,Vmatrix,x,y): #x is the vertical y is the h
    upos = int(Matrix[x-1][y])
    lpos = int(Matrix[x][y-1])
    dpos = int(Matrix[x-1][y-1])
    

    if(Matrix[0][y]==Vmatrix[x]):
        d = dpos+1
        
    else:
        d = dpos-1

    l = lpos-2
    u = upos-2
    f = max(d,l,u)
    if(f==d):
        mem = (x-1,y-1)
    elif(f==u):
        mem = (x-1,y)
    elif(f==l):
        mem = (x,y-1)
    
    return f,mem
mem=[]
M[0] = [' '] + M[0]
if(len(M)%2==0):    
    for i in range(1,len(s1)+1): #change for even 1/odd 2
        M[i]= list(s2[i-1]) + M[i]
else:
    for i in range(1,len(s1)+2): #change for even 1/odd 2
        M[i]= list(s2[i-1]) + M[i]
    


###########ok
s2 = [' ']+s2

for i in range(2,len(M)): #no+1 for odd values
    ram=[]
    for j in range(2,len(M[0])):
        f,r =  check(M,s2,i,j) #i is the vertical line and j is the h
        M[i][j] = f
        ram.append(r)
    mem.append(ram)



# print(M[2][1],M[2][0],M[1][1],M[1][0]) #skip 0,1 values for M 




for i in range(len(M)):
    print(M[i])
print()

for i in range(len(mem)):
    print(mem[i])
match_2=[]
match_1=[]
ch=[]
c1 = len(M)-1
c2 = len(M[0])-1

ch = [c1]+[c2]
print(ch)

while(ch!=[1,1]):
    # print(ch)
    
    match_2.append(M[0][c2])
    match_1.append(M[c1][0])
    ch = list(mem[c1-2][c2-2])
    c1=ch[1]
    c2=ch[0]
    print(ch,' ',c1,c2)
match_1 = list(reversed(match_1))
match_2 = list(reversed(match_2))

print(match_1,match_2)
pt.scatter(match_1,match_2)
pt.show()






