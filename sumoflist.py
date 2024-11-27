n=int(input("enter the number of the terms:"))
a,b=0,1
print("fibonacci series:")
for i in range(n):
    print(a)
    a,b=b,a+b


num= int(input("enter the number:"))
factorial=1
for i in range(1,num+1):
    factorial*=i
print("factorial of",num,"is",factorial)

numbers = [1, 2, 3, 4, 5]
total_sum = sum(numbers)
print("The sum of all items in the list is:", total_sum)