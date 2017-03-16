import math

tests = int(raw_input())

MOD = 10 ** 9 + 7

katalan_number = []
for i in xrange(1, 2001):
    number = math.factorial(2*i)/(math.factorial(i) * math.factorial(i + 1))
    katalan_number.append(number % MOD)

for i in xrange(1, len(katalan_number)):
    katalan_number[i] += katalan_number[i - 1]
    katalan_number[i] %= MOD

#print katalan_number
for _ in xrange(tests):
    n = (int(raw_input()) - 2)/2
    if n == -1:
        print 0
    else:
        print katalan_number[n]