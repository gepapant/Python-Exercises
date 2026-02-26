def get_digits(n):
    a = list(map(int,str(n)))
    return a
    
    
def is_armstrong(n):
    b=get_digits(n)
    athroisma = sum( x**3 for x in b)
    return n==athroisma
        

for num in range(1,999):
    if is_armstrong(num):
        print(num)
        
    
    