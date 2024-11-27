color = input("enter the color by comma separate")
color_list = color.split(',')
print(color_list)

print("First color:", color_list[0])
print("Last color:", color_list[-1])
color_list2 = ["Red", "Orange", "Black", "White"]

print("color-list1 not contained in color-list2 are:")
diff = list(set(color_list) - set(color_list2))
print(diff)
color_int_list = []
for color in color_list:
    color_int_list.append(len(color))
print(f"Lis of integer corresponding to each color:", color_int_list)



