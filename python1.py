import random 
n=random .randint(1,100)
a=-1
gusses=1
while( a!=n):
    a=int(input("gusses the number"))
    if(a>n):
        print("lower number plases")  
        gusses+=1

    elif(a<n):
        print("higher number plases")
        gusses+=1    
       
print(f" gusses number is right {n} in {gusses} attempt")       
       


























