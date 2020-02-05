def compute():
    
    count_prime = 0
    for num in range(2,100000):
        count=0

        if (num<=10):
            for k in range(2,num):
                if (num%k==0 and num!=k):
                    count=1
                    break
            
        elif (num%2==0 or num%3==0 or num%5==0 or num%7==0):
                count =1
        
        
        if(count==0):
            count_prime = count_prime +1
        
        if(count_prime==10001):
            print(num)
            break
            
compute()
