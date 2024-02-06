def is_prime(n):
    if n<2:
     return False
    for i in range(2,int(n/2)+1):
        if(n%i)==0:
            return False
    
    return True 
Numbers=input("Enter numbers separated by space: ").split()
prime=list(filter(lambda x: is_prime(int(x)), Numbers))
print("All numbers: ",Numbers)
print("Prime numbers: ",prime)