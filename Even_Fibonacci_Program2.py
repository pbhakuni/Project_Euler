# Even Fibonacci numbers
# Project Euler Solutions
# https://projecteuler.net/problem=2

def Fibonacci():
    first = 1
    second = 2
    add = 0
    while first <=4000000:
        if first%2 == 0:
            add = add+first
        first,second = second,first+second
    return(str(add))
    
    
if __name__ == "__main__":
    print(Fibonacci())
