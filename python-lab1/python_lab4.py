x=int(input("enter the number:\n"))
divisor=[]
for i in range(1,x+1):
    if x%i==0:
        divisor.append(i)
print ("The divisors of {0} are:{1}".format(x,divisor))
        
    
