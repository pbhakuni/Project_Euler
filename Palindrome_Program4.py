# Program 4 - largest palindrome of 3 digit product
# https://projecteuler.net/problem=4

def compute():
    li = []
    for i in range(1000,100,-1):
        for j in range(1000,100,-1):
            multiply = i *j
            if str(multiply) == str(multiply)[::-1]:
                li.append(multiply)
    return(max(li))            

print(compute())

#913 993 = 906609
