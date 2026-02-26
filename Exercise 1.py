def calculator (a,b,c):
    if a==1:
        return(True , b+c)
    elif a==2:
        return(True , b*c)
    elif a==3:
        return(True , (b+c)/2)
    else:
        return(False , 'Αντικανικονική Κλήση Συνάρτησης')
        
        
for n in (1,2,3,10):
    d=calculator(n,12,28)
    if d:
        print("{:10.2}".format(d))
    else:
        print(d)
        