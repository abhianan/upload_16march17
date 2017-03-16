def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

T=input()
for i in range(T):
    length=input()
    a=map(int, raw_input().split())
    l=[]
    for i in a:
        l.append(i)
    
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
                
    for i in range(length):
        for j in range(length):
            if(i<=j):
                s[i][j]=fib(s[i][j])
                
    sumval=0
    for i in range(length):
        for j in range(length):
            if(i<=j):
                sumval=sumval+s[i][j]
    print sumval% 1000000007