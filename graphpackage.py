from graphics import circle, rectangle
r = int(input("Enter the radius of circle:"))
circle.area_c(r)
circle.peri_c(r)
l = int(input("\nEnter the length of rectangle:"))
b = int(input("\nEnter the breadth of rectangle:"))
rectangle.area_r(l, b)
rectangle.peri_r(l, b)

from graphics.dgraphics import cubiod, sphere
l1 = int(input("\nEnter the length of cubiod:"))
b1 = int(input("\nEnter the breadth of cubiod:"))
h1 = int(input("\nEnter the height of cubiod:"))
cubiod.area_cub(l1, b1, h1)
cubiod.peri_cub(l1, b1, h1)
r1 = int(input("\nEnter the radius of sphere"))
sphere.area_sphere(r1)
sphere.peri_sphere(r1)