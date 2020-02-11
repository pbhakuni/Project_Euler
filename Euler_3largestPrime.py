t = int(input().strip())
li = []

for a0 in range(t):
    n = int(input().strip())
    counter = 0
    for k in range(2,n): #5
        for j in range(1,k): #(1,5)
            if(k%j==0 and k!=j and j!=1):
                counter = 1
                break
        
        if(counter==0):
            li.append(k)
        
        counter =0
            
for pair in itertools.combinations(li,2):
    print(pair)                
                
