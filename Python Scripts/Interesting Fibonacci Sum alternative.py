def fib(input_num):
    temp=0
    temp1=0
    temp2 =1
    if input_num == 1:
        return 0
    if input_num == 2:
        return 1
    else:
        traversal = 2
        while traversal < input_num:
            temp= temp1 + temp2
            temp1 = temp2
            temp2 = temp
            traversal = traversal + 1
        return temp

#recursive solution for subset
def subs(l):
    if l == []:
        return [[]]

    x = subs(l[1:])

    return x + [[l[0]] + y for y in x]    
    
def subse(n):
    m=[]
    for j in range(n):
        m.append(j)
    l= subs(m)
    s=[]
    for i in l:
        if(len(i)==2):
            s.append(i)
    return s

def sumtwo(l,s):
    left=s[0]
    right=s[1]
    sumv=0
    for i in range (left,right+1,1):
        sumv=sumv+l[i]
    return sumv

T=input()
for i in range(T):
    n=input()
    a=map(int, raw_input().split())
    l=[]
    for i in a:
        l.append(i)
 
    sumone=0
    for j in range(n):
        sumone=sumone+fib(l[j]+1)
        
    sumtw=0
    possiblelist=subse(n)
    for k in possiblelist:
        sumtw=sumtw+fib(sumtwo(l,k)+1)
    
    z= sumone+sumtw
    print z% 1000000007

"""
DP to solve above problem
l=[1,2,3,4]
length=len(l)
s=[]
for i in range(length):
    s.append([])
    for j in range(length):
        if(i==j):
            s[i].append(l[i])
        else:
            s[i].append(0)

for i in range(length-1,-1,-1):
    for j in range(length):
        if(i<j):
            s[i][j]=s[i][j-1]+s[i+1][j]-s[i+1][j-1]
print s
"""