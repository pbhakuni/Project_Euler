# Even Fibonacci numbers
# Project Euler Solutions
# https://projecteuler.net/problem=2


t = int(input().strip())

for a0 in range(t):
    first = 1
    second = 2
    third = 3   
    sum = 2
    n = int(input().strip())
    while (third<n):  # 5 < 10
        first = second #5
        second = third #3
        if third%2==0: 
            sum = sum +third #10
        third = first + second #8     
    print(sum)        

