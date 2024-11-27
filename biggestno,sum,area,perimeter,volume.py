pi = 3.1416
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))

if a >= b and a >= c:
    n = a
elif b >= a and b >= c:
    n = b
else:
    n = c

print(f"The biggest number {n}")
nn = n**2
nnn = n**3
sum = n+nn+nnn
print(f"n+nn+nnn= {n} + {nn} + {nnn} = {sum}")

radius = n
area = pi * radius ** 2
perimeter = 2 * pi * radius

print(f"\n for a circle with radius {radius}:")
print(f"area = {area:.2f}")
print(f"perimeter (circumference) = {perimeter:.2f}")
volume = (4/3) * pi * n*n
print("volume of sphere :",volume)