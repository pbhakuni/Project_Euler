
def compute():
    
    count_prime = 1
    for num in range(3,100000,2):
        count=0
        for k in range(3,num,2):
            if (num%k==0 and num!=k):
                count=1
                break
        
        if(count==0):
            count_prime = count_prime +1

        if(count_prime==10001):
            return(num)
            
print(compute())
