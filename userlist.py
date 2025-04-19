# a = []

# n = int(input("Enter the number of elements: "))

# for i in range(n):
#     a.append(input("Enter the element: "))

# for i in range(n):
#     a.append(input("Enter the element: "))

# print(a)



# for elements in dir(list):
#     if elements.startswith("__"):
#         pass
#     else:
#         print(elements)

for elements in dir(list):
    if "__" not in elements:
        print(elements)
