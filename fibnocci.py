n=int(input("enter the number of the terms:"))
a,b=0,1
print("fibonacci series:")
for i in range(n):
    print(a)
    a,b=b,a+b
