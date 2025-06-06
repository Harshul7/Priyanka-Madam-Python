
# HCF or GCD of two numbers using 
a=int(input("Enter value of a"))
b=int(input("Enter value of b"))
a1=a
b1=b
booleanVar= False
if a==0:
    print("GCD=",b)
    booleanVar= True
elif b==0:
    print("GCD=",a)
    booleanVar=True
#Why did the code not stop after exit(0) ? -> Doubt
   
while b!=0 and (not booleanVar):
    a,b=b,a%b 
#a=12 and b=24 
''' a=24,b=12
    a=12,b=0
    since b==0,GCD=a=12 '''
if not booleanVar:
    print("GCD of a=",a1,"and b=",b1,"is ",a)
