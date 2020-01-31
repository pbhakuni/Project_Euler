multiply = 1

def compute():
    for i in range(1000,100,-1):
        for j in range(1000,100,-1):
            multiply = i *j
            if str(multiply) == str(multiply)[::-1]:
                return(multiply)


print(compute())
        
