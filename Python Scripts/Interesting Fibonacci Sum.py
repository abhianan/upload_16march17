from itertools import combinations, chain

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

def subse(n):
    allsubsets = lambda n: list(chain(*[combinations(range(n), ni) for ni in range(n+1)]))
    l= allsubsets(n)
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
https://www.hackerrank.com/contests/walmart-codesprint-algo/challenges/fibonacci-sum-1

Tuzki's love for Fibonacci numbers led him to formulate the following interesting function, , on an array, :

where  denotes the sum of array 's elements and  denotes the  Fibonacci number.

Tuzki is so obsessed with this interesting function that he decides to calculate the following expression, , accurately and efficiently:

This is a tough task for Tuzki and he can't do it alone! Given the values of  and array  for  queries, help Tuzki by finding and printing the value of  modulo  on a new line for each query.

Input Format

The first line contains a single integer, , denoting the number of queries. The  subsequent lines describe each query over two lines:

The first line of each query contains an integer, , denoting the size of array .
The second line of each query contains  space-separated integers denoting the respective values of array .
"""