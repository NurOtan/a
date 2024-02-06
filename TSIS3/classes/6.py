def is_prime(n):
    if n<2:
     return False
    for i in range(2,int(n/2)+1):
        if(n%i)==0:
            return False
    
    return True 

Numbers=input("Enter numbers separated by space: ").split()
prime=list(())
print("All numbers: ",Numbers)
for i in Numbers:
    if is_prime(int(i)):
        prime.append(i)
        
print ("Prime numbers: ",prime)